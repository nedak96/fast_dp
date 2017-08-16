#!/usr/bin/env python
# fast_dp.py
#
# A *quick* data reduction jiffy, for the purposes of providing an estimate
# of the quality of a data set as fast as possible along with a set of
# intensities which have been scaled reasonably well. This relies heavily on
# XDS, and forkintegrate in particular.

import sys
import os
import time
import copy
import exceptions
import traceback

if not 'FAST_DP_ROOT' in os.environ:
    raise RuntimeError, 'FAST_DP_ROOT not defined'

fast_dp_lib = os.path.join(os.environ['FAST_DP_ROOT'], 'lib')

if not fast_dp_lib in sys.path:
    sys.path.append(fast_dp_lib)

from run_job import get_number_cpus
from cell_spacegroup import check_spacegroup_name, check_split_cell, \
     generate_primitive_cell
from xml_output import write_ispyb_xml

from image_readers import read_image_metadata, check_file_readable

from autoindex import autoindex
from integrate import integrate
from scale import scale
from merge import merge
from pointgroup import decide_pointgroup, getRes
from logger import write
from shutil import copyfile, rmtree
import numpy as np

class FastDP:
    '''A class to implement fast data processing for MX beamlines (at Diamond)
    which uses XDS, Pointless, Scala and a couple of other CCP4 odds and
    ends to provide integrated and scaled data in a couple of minutes.'''

    def __init__(self):

        # unguessable input parameters
        self._start_image = None

        # optional user inputs - the unit cell is needed twice, once for the
        # correct lattice and once for the primitive lattice which will
        # be determined from this...

        self._input_spacegroup = None
        self._input_cell = None

        # this is assigned automatically from the input cell above
        self._input_cell_p1 = None

        # user controlled resolution limits
        self._resolution_low = 30.0
        self._resolution_high = 0.0

        # job control see -j -J -k command-line options below
        self._n_jobs = 1
        self._n_cores = 0
        self._max_n_jobs = 0
        self._n_cpus = get_number_cpus()

        # image ranges
        self._first_image = None
        self._last_image = None

        # internal data
        self._metadata = None

        # these are the resulting not input ones... clarify this?
        self._p1_unit_cell = None
        self._unit_cell = None
        self._space_group_number = None

        # two additional results

        self._nref = 0
        self._xml_results = None
        self._refined_beam = (0, 0)

        return

    def set_n_jobs(self, n_jobs):
        self._n_jobs = n_jobs
        return

    def set_n_cores(self, n_cores):
        self._n_cores = n_cores
        return

    def set_max_n_jobs(self, max_n_jobs):
        self._max_n_jobs = max_n_jobs
        return

    def set_first_image(self, first_image):
        self._first_image = first_image
        return

    def set_last_image(self, last_image):
        self._last_image = last_image
        return

    def set_resolution_low(self, resolution_low):
        self._resolution_low = resolution_low
        return

    def set_resolution_high(self, resolution_high):
        self._resolution_high = resolution_high
        return

    def set_start_image(self, start_image):
        '''Set the image to work from: in the majority of cases this will
        be sufficient. This returns a list of image numbers which may be
        missing.'''

        assert(self._start_image is None)

        # check input is image file
        import os
        if not os.path.isfile(start_image):
            raise RuntimeError, 'no image provided: data collection cancelled?'

        check_file_readable(start_image)

        self._start_image = start_image
        self._metadata = read_image_metadata(self._start_image)

        # check that all of the images are present

        matching = self._metadata['matching']

        missing = []

        for j in range(min(matching), max(matching)):
            if not j in matching:
                missing.append(j)

        return missing

    def set_beam(self, beam):
        '''Set the beam centre, in mm, in the Mosflm reference frame.'''

        assert(self._metadata)
        assert(len(beam) == 2)

        self._metadata['beam'] = beam

        return

    def set_atom(self, atom):
        '''Set the heavy atom, if appropriate.'''

        assert(self._metadata)

        self._metadata['atom'] = atom

        return

    # N.B. these two methods assume that the input unit cell etc.
    # has already been tested at the option parsing stage...

    def set_input_spacegroup(self, input_spacegroup):
        self._input_spacegroup = input_spacegroup
        return

    def set_input_cell(self, input_cell):

        self._input_cell = input_cell

        # convert this to a primitive cell based on the centring
        # operation implied by the spacegroup

        assert(self._input_spacegroup)

        self._input_cell_p1 = generate_primitive_cell(
            self._input_cell, self._input_spacegroup).parameters()

        return

    def _read_image_metadata(self):
        '''Get the information from the start image to the metadata bucket.
        For internal use only.'''

        assert(self._start_image)

        return

    def get_metadata_item(self, item):
        '''Get a specific item from the metadata.'''

        assert(self._metadata)
        assert(item in self._metadata)

        return self._metadata[item]

    def process(self):
        '''Main routine, chain together all of the steps imported from
        autoindex, integrate, pointgroup, scale and merge.'''

        try:

            hostname = os.environ['HOSTNAME'].split('.')[0]
            write('Running on: %s' % hostname)

        except:
            pass

        # check input frame limits

        if not self._first_image is None:
            if self._metadata['start'] < self._first_image:
                start = self._metadata['start']
                self._metadata['start'] = self._first_image
                self._metadata['phi_start'] += self._metadata['phi_width'] * \
                                               (self._first_image - start)

        if not self._last_image is None:
            if self._metadata['end'] > self._last_image:
                self._metadata['end'] = self._last_image

        # first if the number of jobs was set to 0, decide something sensible.
        # this should be jobs of a minimum of 5 degrees, 10 frames.

        if self._n_jobs == 0:
            phi = self._metadata['oscillation'][1]

            if phi == 0.0:
                raise RuntimeError, 'grid scan data'

            wedge = max(10, int(round(5.0 / phi)))
            frames = self._metadata['end'] - self._metadata['start'] + 1
            n_jobs = int(round(frames / wedge))
            if self._max_n_jobs > 0:
                if n_jobs > self._max_n_jobs:
                    n_jobs = self._max_n_jobs
            self.set_n_jobs(n_jobs)

        write('Number of jobs: %d' % self._n_jobs)
        write('Number of cores: %d' % self._n_cores)

        step_time = time.time()

        write('Processing images: %d -> %d' % (self._metadata['start'],
                                               self._metadata['end']))

        phi_end = self._metadata['phi_start'] + self._metadata['phi_width'] * \
                  (self._metadata['end'] - self._metadata['start'] + 1)

        write('Phi range: %.2f -> %.2f' % (self._metadata['phi_start'],
                                           phi_end))

        write('Template: %s' % self._metadata['template'])
        write('Wavelength: %.5f' % self._metadata['wavelength'])
        write('Working in: %s' % os.getcwd())

        try:
            self._p1_unit_cell = autoindex(self._metadata,
                                           input_cell = self._input_cell_p1)
        except exceptions.Exception, e:
            traceback.print_exc(file = open('fast_dp_pro.error', 'w'))
            write('Autoindexing error: %s' % e)
            return

        try:
            mosaics = integrate(self._metadata, self._p1_unit_cell,
                                self._resolution_low, self._n_jobs,
                                self._n_cores)
            write('Mosaic spread: %.2f < %.2f < %.2f' % tuple(mosaics))
        except RuntimeError, e:
            traceback.print_exc(file = open('fast_dp_pro.error', 'w'))
            write('Integration error: %s' % e)
            return

        try:

            # FIXME in here will need a mechanism to take the input
            # spacegroup, determine the corresponding pointgroup
            # and then apply this (or verify that it is allowed then
            # select)

            metadata = copy.deepcopy(self._metadata)

            cell, sg_num, resol = decide_pointgroup(
                self._p1_unit_cell, metadata,
                input_spacegroup = self._input_spacegroup)
            self._unit_cell = cell
            self._space_group_number = sg_num

            if not self._resolution_high:
                self._resolution_high = resol

        except RuntimeError, e:
            write('Pointgroup error: %s' % e)
            return

	nq = len(self._metadata['template'].split(".")[0])-len(self._metadata['template'].split("?")[0])
	n10 = int((self._metadata['end']-self._metadata['start']+1)/10)
	np10 = n10*self._metadata['phi_width']
	origPhiEnd = phi_end
	origPhiStart = self._metadata['phi_start']
	origEnd = self._metadata['end']
	origStart = self._metadata['start']
	cPath = os.getcwd()
	results = [None for y in range(0,55)]
	uc = sg = nref = rb = None
	i = 0
	for x in range(0, 10):
		phi_end = origPhiEnd
		self._metadata['end'] = origEnd
		for y in range(0, 10-x):
			tPath = cPath+"/"+str(self._metadata['start'])+"-"+str(self._metadata['end'])
			if not os.path.exists(tPath):
				os.makedirs(tPath)
			copyfile("INTEGRATE.HKL", tPath+"/INTEGRATE.HKL")
			copyfile("X-CORRECTIONS.cbf", tPath+"/X-CORRECTIONS.cbf")
			copyfile("Y-CORRECTIONS.cbf", tPath+"/Y-CORRECTIONS.cbf")
			os.chdir(tPath)
			tfile = open(self._metadata['template'].split("?")[0]+str(self._metadata['start'])+"-"+str(self._metadata['end'])+"_fast_dp_pro.log", "w")
			self._resolution_high = getRes(self._p1_unit_cell, self._metadata)
			try:
				uc, sg, nref, beam_pixels = \
				scale(self._unit_cell, self._metadata, self._space_group_number, \
				   self._resolution_high)
				rb = (self._metadata['pixel'][1] * beam_pixels[1],
					              self._metadata['pixel'][0] * beam_pixels[0])
				self._nref += nref

			except RuntimeError, e:
				write('Scaling error: %s' % e)
				return

			try:
				n_images = self._metadata['end'] - self._metadata['start'] + 1
				results[i] = merge()
			except RuntimeError, e:
				write('Merging error: %s' % e)
				return
			results[i]['sg'] = sg
			results[i]['uc'] = uc
			results[i]['start'] = self._metadata['start']
			results[i]['end'] = self._metadata['end']
			results[i]['phi_start'] = self._metadata['phi_start']
			results[i]['zx'] = 9-x-y
			results[i]['zy'] = 9-x
			results[i]['n10'] = n10
			results[i]['np10'] = np10
			results[i]['ops'] = origPhiStart
			results[i]['ope'] = origPhiEnd

			write_ispyb_xml(self._commandline, sg, uc, results[i], self._metadata['template'].replace('?'*nq, str(results[i]['start']+origStart-1).zfill(nq)), rb)

			tfile.write('Range: ' + str(results[i]['start']) + ' -> ' + str(results[i]['end']))
			tfile.write('\n%20s ' % 'Low resolution'     + '%6.2f ' % results[i]['resol_low_overall'] + '%6.2f ' % results[i]['resol_low_inner']  + '%6.2f\n' % results[i]['resol_low_outer'])
			tfile.write('%20s ' % 'High resolution'    + '%6.2f ' % results[i]['resol_high_overall'] + '%6.2f ' % results[i]['resol_high_inner']  + '%6.2f\n' % results[i]['resol_high_outer'])
			tfile.write('%20s ' % 'Rmerge'             + '%6.3f ' % results[i]['rmerge_overall'] + '%6.3f ' % results[i]['rmerge_inner']  + '%6.3f\n' % results[i]['rmerge_outer'])
			tfile.write('%20s ' % 'Rpim'             + '%6.3f ' % results[i]['rpim_overall'] + '%6.3f ' % results[i]['rpim_inner']  + '%6.3f\n' % results[i]['rpim_outer'])
			tfile.write('%20s ' % 'I/sigma'            + '%6.2f ' % results[i]['isigma_overall'] + '%6.2f ' % results[i]['isigma_inner']  + '%6.2f\n' % results[i]['isigma_outer'])
			tfile.write('%20s ' % 'Completeness'       + '%6.1f ' % results[i]['completeness_overall'] + '%6.1f ' % results[i]['completeness_inner']  + '%6.1f\n' % results[i]['completeness_outer'])
			tfile.write('%20s ' % 'Multiplicity'       + '%6.1f ' % results[i]['multiplicity_overall'] + '%6.1f ' % results[i]['multiplicity_inner']  + '%6.1f\n' % results[i]['multiplicity_outer'])
			tfile.write('%20s ' % 'CC 1/2'             + '%6.1f ' % results[i]['cchalf_overall'] + '%6.1f ' % results[i]['cchalf_inner']  + '%6.1f\n' % results[i]['cchalf_outer'])
			tfile.write('%20s ' % 'Anom. Completeness' + '%6.1f ' % results[i]['acompleteness_overall'] + '%6.1f ' % results[i]['acompleteness_inner']  + '%6.1f\n' % results[i]['acompleteness_outer'])
			tfile.write('%20s ' % 'Anom. Multiplicity' + '%6.1f ' % results[i]['amultiplicity_overall'] + '%6.1f ' % results[i]['amultiplicity_inner']  + '%6.1f\n' % results[i]['amultiplicity_outer'])
			tfile.write('%20s ' % 'Anom. Correlation'  + '%6.1f ' % results[i]['ccanom_overall'] + '%6.1f ' % results[i]['ccanom_inner']  + '%6.1f\n' % results[i]['ccanom_outer'])
			tfile.write('%20s ' % 'Nrefl'              + '%6d ' % results[i]['nref_overall'] + '%6d ' % results[i]['nref_inner']  + '%6d\n' % results[i]['nref_outer'])
			tfile.write('%20s ' % 'Nunique'            + '%6d ' % results[i]['nunique_overall'] + '%6d ' % results[i]['nunique_inner']  + '%6d\n' % results[i]['nunique_outer'])
			i += 1
			copyfile("fast_dp_pro.mtz", self._metadata['template'].split("?")[0]+str(self._metadata['start'])+"-"+str(self._metadata['end'])+"_fast_dp_pro.mtz")
			tfile.close()
			self._metadata['end'] -= n10
			phi_end -= np10
			os.chdir(cPath)
			print ' [' + ('-'*i) + (' '*(55-i)) + ']\r',
		self._metadata['start'] += n10
		self._metadata['phi_start'] += np10
	np.save('results.npy', results)
	results = sorted(results, key=lambda k : (k['rmerge_overall'], -k['completeness_overall']))
	c = 0
	i = 0
	write(80 * '-')
	while i<55 and c<20:
		if results[i]['completeness_overall'] > 97:
			if c == 0:
				bestPath = str(results[i]['start']) + '-' + str(results[i]['end']) + "(BestRange)"
				if os.path.exists(bestPath):
					rmtree(bestPath, ignore_errors=False, onerror=None)
				os.rename(str(results[i]['start']) + '-' + str(results[i]['end']), bestPath)
				write('Best range: ' + str(results[i]['start']) + ' -> ' + str(results[i]['end']))
				self._xml_results = results[i]
			else:
				write(str(c+1) + ' range: ' + str(results[i]['start']) + ' -> ' + str(results[i]['end']))
			write('%20s ' % 'Low resolution'     + '%6.2f ' % results[i]['resol_low_overall'] + '%6.2f ' % results[i]['resol_low_inner']  + '%6.2f' % results[i]['resol_low_outer'])
			write('%20s ' % 'High resolution'    + '%6.2f ' % results[i]['resol_high_overall'] + '%6.2f ' % results[i]['resol_high_inner']  + '%6.2f' % results[i]['resol_high_outer'])
			write('%20s ' % 'Rmerge'             + '%6.3f ' % results[i]['rmerge_overall'] + '%6.3f ' % results[i]['rmerge_inner']  + '%6.3f' % results[i]['rmerge_outer'])
			write('%20s ' % 'Rpim'             + '%6.3f ' % results[i]['rpim_overall'] + '%6.3f ' % results[i]['rpim_inner']  + '%6.3f' % results[i]['rpim_outer'])
			write('%20s ' % 'I/sigma'            + '%6.2f ' % results[i]['isigma_overall'] + '%6.2f ' % results[i]['isigma_inner']  + '%6.2f' % results[i]['isigma_outer'])
			write('%20s ' % 'Completeness'       + '%6.1f ' % results[i]['completeness_overall'] + '%6.1f ' % results[i]['completeness_inner']  + '%6.1f' % results[i]['completeness_outer'])
			write('%20s ' % 'Multiplicity'       + '%6.1f ' % results[i]['multiplicity_overall'] + '%6.1f ' % results[i]['multiplicity_inner']  + '%6.1f' % results[i]['multiplicity_outer'])
			write('%20s ' % 'CC 1/2'             + '%6.1f ' % results[i]['cchalf_overall'] + '%6.1f ' % results[i]['cchalf_inner']  + '%6.1f' % results[i]['cchalf_outer'])
			write('%20s ' % 'Anom. Completeness' + '%6.1f ' % results[i]['acompleteness_overall'] + '%6.1f ' % results[i]['acompleteness_inner']  + '%6.1f' % results[i]['acompleteness_outer'])
			write('%20s ' % 'Anom. Multiplicity' + '%6.1f ' % results[i]['amultiplicity_overall'] + '%6.1f ' % results[i]['amultiplicity_inner']  + '%6.1f' % results[i]['amultiplicity_outer'])
			write('%20s ' % 'Anom. Correlation'  + '%6.1f ' % results[i]['ccanom_overall'] + '%6.1f ' % results[i]['ccanom_inner']  + '%6.1f' % results[i]['ccanom_outer'])
			write('%20s ' % 'Nrefl'              + '%6d ' % results[i]['nref_overall'] + '%6d ' % results[i]['nref_inner']  + '%6d' % results[i]['nref_outer'])
			write('%20s ' % 'Nunique'            + '%6d ' % results[i]['nunique_overall'] + '%6d ' % results[i]['nunique_inner']  + '%6d' % results[i]['nunique_outer'])
			write(80 * '-')
			c += 1
		i += 1

	if c == 0:
		write('No data meets the requirements')
		write(80 * '-')

        write('Merging point group: %s' % self._xml_results['sg'])
        write('Unit cell: %6.2f %6.2f %6.2f %6.2f %6.2f %6.2f' % \
              self._xml_results['uc'])

        duration = time.time() - step_time
        write('Processing took %s (%d s)' %
              (time.strftime('%Hh %Mm %Ss', time.gmtime(duration)), duration))
	copyfile("fast_dp_pro.log", self._metadata['template'].split("?")[0]+"fast_dp_pro.log")
        return

def main():
    '''Main routine for fast_dp.'''

    import os
    os.environ['FAST_DP_FORKINTEGRATE'] = '1'

    from optparse import OptionParser

    commandline = ' '.join(sys.argv)

    parser = OptionParser()

    parser.add_option('-b', '--beam', dest = 'beam',
                      help = 'Beam centre: x, y (mm)')

    parser.add_option('-a', '--atom', dest = 'atom',
                      help = 'Atom type (e.g. Se)')

    parser.add_option('-j', '--number-of-jobs', dest = 'number_of_jobs',
                      help = 'Number of jobs for integration')
    parser.add_option('-k', '--number-of-cores', dest = 'number_of_cores',
                      help = 'Number of cores for integration')
    parser.add_option('-J', '--maximum-number-of-jobs',
                      dest = 'maximum_number_of_jobs',
                      help = 'Maximum number of jobs for integration')

    parser.add_option('-c', '--cell', dest = 'cell',
                      help = 'Cell constants for processing, needs spacegroup')
    parser.add_option('-s', '--spacegroup', dest = 'spacegroup',
                      help = 'Spacegroup for scaling and merging')

    parser.add_option('-1', '--first-image', dest = 'first_image',
                      help = 'First image for processing')
    parser.add_option('-N', '--last-image', dest = 'last_image',
                      help = 'First image for processing')

    parser.add_option('-r', '--resolution-high', dest = 'resolution_high',
                      help = 'High resolution limit')
    parser.add_option('-R', '--resolution-low', dest = 'resolution_low',
                      help = 'Low resolution limit')

    (options, args) = parser.parse_args()

    assert(len(args) == 1)

    image = args[0]

    try:
        fast_dp = FastDP()
        fast_dp._commandline = commandline
        write('Fast_DP installed in: %s' % os.environ['FAST_DP_ROOT'])
        write('Starting image: %s' % image)
        missing = fast_dp.set_start_image(image)
        if options.beam:
            x, y = tuple(map(float, options.beam.split(',')))
            fast_dp.set_beam((x, y))

        if options.atom:
            fast_dp.set_atom(options.atom)

        if options.maximum_number_of_jobs:
            fast_dp.set_max_n_jobs(int(options.maximum_number_of_jobs))

        if options.number_of_jobs:
            if options.maximum_number_of_jobs:
                n_jobs = min(int(options.number_of_jobs),
                             int(options.maximum_number_of_jobs))
            else:
                n_jobs = int(options.number_of_jobs)
            fast_dp.set_n_jobs(n_jobs)

        if options.number_of_cores:
            n_cores = int(options.number_of_cores)
            fast_dp.set_n_cores(n_cores)

        if options.first_image:
            first_image = int(options.first_image)
            missing = [m for m in missing if m >= first_image]
            fast_dp.set_first_image(first_image)

        if options.last_image:
            last_image = int(options.last_image)
            missing = [m for m in missing if m <= last_image]
            fast_dp.set_last_image(last_image)

        if missing:
            raise RuntimeError, 'images missing: %s' % \
                ' '.join(map(str, missing))

        if options.resolution_low:
            fast_dp.set_resolution_low(float(options.resolution_low))

        if options.resolution_high:
            fast_dp.set_resolution_high(float(options.resolution_high))

        # must input spacegroup first as unpacking of the unit cell
        # will depend on the centering operation...

        if options.spacegroup:
            try:
                spacegroup = check_spacegroup_name(options.spacegroup)
                fast_dp.set_input_spacegroup(spacegroup)
                write('Set spacegroup: %s' % spacegroup)
            except RuntimeError, e:
                write('Spacegroup %s not recognised: ignoring' % \
                      options.spacegroup)

        if options.cell:
            assert(options.spacegroup)
            cell = check_split_cell(options.cell)
            write('Set cell: %.2f %.2f %.2f %.2f %.2f %.2f' % cell)
            fast_dp.set_input_cell(cell)

        fast_dp.process()

    except exceptions.Exception, e:
        traceback.print_exc(file = open('fast_dp_pro.error', 'w'))
        write('Fast DP error: %s' % str(e))

    json_stuff = { }
    for prop in dir(fast_dp):
        ignore = ['_read_image_metadata']
        if not prop.startswith('_') or prop.startswith('__'):
            continue
        if prop in ignore:
            continue
        json_stuff[prop] = getattr(fast_dp, prop)
    import json
    json.dump(json_stuff, open('fast_dp_pro.json', 'wb'))

    return

if __name__ == '__main__':

    main()
