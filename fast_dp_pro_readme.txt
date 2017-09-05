For FastDP Pro run FastDP as you normal would, but use add -p.  It will now output up to 20 results based on the best rMerge values with completenesses of over 97.  To view the rest of the data, and graphs, run fast_dp_gui in the same directory you ran FastDP.

kbadalian@cpu-009:~/nfdp$ fast_dp KNA004_C5_350_master.h5
Fast_DP installed in: /home/kbadalian/fast_dp_pro
Starting image: KNA004_C5_350_master.h5
Reading KNA004_C5_350_master.h5 took 2.15s
Number of jobs: 1
Number of cores: 40
Processing images: 1 -> 900
Phi range: 0.00 -> 180.00
Template: KNA004_C5_350_??????.h5
Wavelength: 0.97913
Working in: /home/kbadalian/nfdp
All autoindexing results:
Lattice      a      b      c  alpha   beta  gamma
     tP  81.20  81.20 166.50  90.00  90.00  90.00
     oC 114.90 114.90 166.50  90.00  90.00  90.00
     oP  81.20  81.20 166.50  90.00  90.00  90.00
     mC 114.90 114.90 166.50  90.00  90.10  90.00
     mP  81.20  81.20 166.50  90.00  90.10  90.00
     aP  81.20  81.20 166.50  90.10  90.10  90.00
Mosaic spread: 0.10 < 0.14 < 0.23
Happy with sg# 89
 81.40  81.40 166.90  90.00  90.00  90.00
--------------------------------------------------------------------------------
      Low resolution  29.20  29.20   2.71
     High resolution   2.64  11.82   2.64
              Rmerge  0.248  0.125  1.086
             I/sigma   8.70  18.30   1.90
        Completeness   99.3   93.7   91.7
        Multiplicity   12.9   10.2   11.9
              CC 1/2  0.986  0.993  0.867
  Anom. Completeness   99.2   97.3   89.3
  Anom. Multiplicity    6.7    7.2    6.1
   Anom. Correlation -0.103  0.122 -0.169
               Nrefl 221772   2372  13331
             Nunique  17214    232   1122
           Mid-slope  0.782
                dF/F  0.101
          dI/sig(dI)  0.722
--------------------------------------------------------------------------------
Merging point group: P 4 2 2
Unit cell:  81.65  81.65 167.14  90.00  90.00  90.00
Processing took 00h 01m 57s (117 s) [221910 reflections]
RPS: 1884.6
kbadalian@cpu-009:~/nfdp$ fast_dp KNA004_C5_350_master.h5 -p
Fast_DP installed in: /home/kbadalian/fast_dp_pro
Starting image: KNA004_C5_350_master.h5
Reading KNA004_C5_350_master.h5 took 2.21s
Number of jobs: 1
Number of cores: 40
Processing images: 1 -> 900
Phi range: 0.00 -> 180.00
Template: KNA004_C5_350_??????.h5
Wavelength: 0.97913
Working in: /home/kbadalian/nfdp
All autoindexing results:
Lattice      a      b      c  alpha   beta  gamma
     tP  81.20  81.20 166.50  90.00  90.00  90.00
     oC 114.90 114.90 166.50  90.00  90.00  90.00
     oP  81.20  81.20 166.50  90.00  90.00  90.00
     mC 114.90 114.90 166.50  90.00  90.10  90.00
     mP  81.20  81.20 166.50  90.00  90.10  90.00
     aP  81.20  81.20 166.50  90.10  90.10  90.00
Mosaic spread: 0.10 < 0.14 < 0.23
Happy with sg# 89
 81.40  81.40 166.90  90.00  90.00  90.00
--------------------------------------------------------------------------------
Best range: 1 -> 270
      Low resolution  29.17  29.17   2.26
     High resolution   2.21   9.87   2.21
              Rmerge  0.120  0.071  0.650
                Rpim  0.091  0.056  0.510
             I/sigma   6.40  14.70   1.50
        Completeness   98.8   95.8   87.8
        Multiplicity    4.0    3.4    3.8
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   93.5   98.0   79.1
  Anom. Multiplicity    2.0    2.0    2.0
   Anom. Correlation    0.0    0.3   -0.1
               Nrefl 114013   1305   7007
             Nunique  28813    386   1843
--------------------------------------------------------------------------------
2 range: 1 -> 360
      Low resolution  29.17  29.17   2.35
     High resolution   2.29  10.26   2.29
              Rmerge  0.140  0.091  0.676
                Rpim  0.092  0.058  0.470
             I/sigma   6.90  14.70   1.70
        Completeness   98.7   95.6   85.0
        Multiplicity    5.2    4.5    4.8
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   96.5   97.7   75.5
  Anom. Multiplicity    2.7    2.7    2.7
   Anom. Correlation    0.0   -0.0   -0.0
               Nrefl 135175   1549   7805
             Nunique  25752    347   1611
--------------------------------------------------------------------------------
3 range: 181 -> 450
      Low resolution  29.16  29.16   2.57
     High resolution   2.50  11.19   2.50
              Rmerge  0.141  0.087  0.674
                Rpim  0.105  0.064  0.508
             I/sigma   5.60  11.70   1.20
        Completeness   97.8   89.4   87.4
        Multiplicity    4.0    3.5    3.6
              CC 1/2    1.0    1.0    0.5
  Anom. Completeness   93.0   90.2   78.0
  Anom. Multiplicity    2.1    2.1    2.0
   Anom. Correlation   -0.0    0.4    0.0
               Nrefl  79840    904   4580
             Nunique  19732    256   1278
--------------------------------------------------------------------------------
4 range: 91 -> 450
      Low resolution  29.20  29.20   2.49
     High resolution   2.43  10.85   2.43
              Rmerge  0.151  0.096  0.763
                Rpim  0.099  0.061  0.513
             I/sigma   6.40  13.50   1.30
        Completeness   98.1   91.3   87.5
        Multiplicity    5.3    4.6    4.5
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   94.4   93.2   73.9
  Anom. Multiplicity    2.7    2.9    2.5
   Anom. Correlation   -0.0    0.1   -0.1
               Nrefl 115980   1323   6319
             Nunique  21750    286   1394
--------------------------------------------------------------------------------
5 range: 271 -> 540
      Low resolution  29.20  29.20   2.80
     High resolution   2.72  12.18   2.72
              Rmerge  0.154  0.093  0.755
                Rpim  0.128  0.081  0.624
             I/sigma   5.60  10.10   1.30
        Completeness   98.7   92.6   90.8
        Multiplicity    4.0    3.4    3.8
              CC 1/2    1.0    1.0    0.6
  Anom. Completeness   95.0   97.0   81.0
  Anom. Multiplicity    2.1    2.4    2.1
   Anom. Correlation   -0.0    0.3   -0.1
               Nrefl  62466    702   3891
             Nunique  15550    208   1022
--------------------------------------------------------------------------------
6 range: 181 -> 540
      Low resolution  29.17  29.17   2.65
     High resolution   2.58  11.55   2.58
              Rmerge  0.157  0.096  0.813
                Rpim  0.111  0.069  0.577
             I/sigma   6.50  12.80   1.30
        Completeness   99.1   93.9   90.2
        Multiplicity    5.3    4.4    4.9
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.2   97.5   82.7
  Anom. Multiplicity    2.8    2.8    2.7
   Anom. Correlation   -0.0    0.1   -0.0
               Nrefl  97605   1081   5907
             Nunique  18322    247   1206
--------------------------------------------------------------------------------
7 range: 1 -> 450
      Low resolution  29.18  29.18   2.41
     High resolution   2.35  10.52   2.35
              Rmerge  0.162  0.104  0.739
                Rpim  0.096  0.059  0.454
             I/sigma   7.10  15.10   1.60
        Completeness   99.0   95.4   87.7
        Multiplicity    6.5    5.5    5.7
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   97.6   98.2   75.5
  Anom. Multiplicity    3.3    3.5    3.1
   Anom. Correlation   -0.0   -0.1   -0.0
               Nrefl 156682   1792   8730
             Nunique  23985    324   1535
--------------------------------------------------------------------------------
8 range: 91 -> 540
      Low resolution  29.21  29.21   2.56
     High resolution   2.50  11.16   2.50
              Rmerge  0.167  0.103  0.794
                Rpim  0.102  0.062  0.499
             I/sigma   7.10  14.40   1.50
        Completeness   99.1   94.5   89.6
        Multiplicity    6.6    5.5    5.7
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.5   97.8   83.2
  Anom. Multiplicity    3.5    3.6    3.1
   Anom. Correlation   -0.0    0.0   -0.1
               Nrefl 134261   1518   7603
             Nunique  20318    278   1326
--------------------------------------------------------------------------------
9 range: 181 -> 630
      Low resolution  29.19  29.19   2.74
     High resolution   2.67  11.95   2.67
              Rmerge  0.174  0.107  0.863
                Rpim  0.108  0.065  0.526
             I/sigma   7.20  13.90   1.60
        Completeness   99.1   93.6   89.2
        Multiplicity    6.6    5.4    6.3
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.9   97.2   86.3
  Anom. Multiplicity    3.5    3.6    3.4
   Anom. Correlation   -0.0    0.3   -0.1
               Nrefl 109871   1221   6775
             Nunique  16607    225   1077
--------------------------------------------------------------------------------
10 range: 271 -> 630
      Low resolution  29.25  29.25   2.85
     High resolution   2.78  12.43   2.78
              Rmerge  0.174  0.105  0.885
                Rpim  0.122  0.072  0.623
             I/sigma   6.30  11.60   1.40
        Completeness   98.9   92.2   91.8
        Multiplicity    5.3    4.5    5.1
              CC 1/2    1.0    1.0    0.6
  Anom. Completeness   98.6   96.8   88.6
  Anom. Multiplicity    2.9    3.2    2.7
   Anom. Correlation   -0.0    0.1   -0.1
               Nrefl  78730    873   5081
             Nunique  14773    196    990
--------------------------------------------------------------------------------
11 range: 1 -> 540
      Low resolution  29.18  29.18   2.45
     High resolution   2.38  10.66   2.38
              Rmerge  0.180  0.110  0.826
                Rpim  0.098  0.058  0.477
             I/sigma   7.40  15.70   1.60
        Completeness   99.2   95.4   89.5
        Multiplicity    7.8    6.5    6.4
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.4   98.1   81.3
  Anom. Multiplicity    4.0    4.3    3.4
   Anom. Correlation   -0.0   -0.1   -0.1
               Nrefl 180988   2064   9590
             Nunique  23161    318   1493
--------------------------------------------------------------------------------
12 range: 91 -> 630
      Low resolution  29.22  29.22   2.65
     High resolution   2.59  11.57   2.59
              Rmerge  0.183  0.112  0.905
                Rpim  0.100  0.061  0.505
             I/sigma   7.80  15.40   1.60
        Completeness   99.3   94.1   91.4
        Multiplicity    7.9    6.5    7.2
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.0   97.5   87.5
  Anom. Multiplicity    4.2    4.4    3.9
   Anom. Correlation   -0.0    0.3   -0.1
               Nrefl 145789   1604   8860
             Nunique  18363    248   1223
--------------------------------------------------------------------------------
13 range: 1 -> 630
      Low resolution  29.19  29.19   2.56
     High resolution   2.49  11.15   2.49
              Rmerge  0.193  0.114  0.830
                Rpim  0.096  0.055  0.440
             I/sigma   8.10  16.50   1.80
        Completeness   99.3   94.8   90.8
        Multiplicity    9.2    7.4    7.8
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.0   97.8   87.3
  Anom. Multiplicity    4.9    5.1    4.2
   Anom. Correlation   -0.0    0.1   -0.2
               Nrefl 186748   2071  10499
             Nunique  20347    279   1344
--------------------------------------------------------------------------------
14 range: 181 -> 720
      Low resolution  29.21  29.21   2.83
     High resolution   2.75  12.32   2.75
              Rmerge  0.197  0.109  1.068
                Rpim  0.109  0.059  0.588
             I/sigma   7.60  14.80   1.50
        Completeness   99.3   93.0   91.3
        Multiplicity    7.8    6.3    7.5
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.0   96.8   88.1
  Anom. Multiplicity    4.2    4.4    4.1
   Anom. Correlation   -0.0    0.6   -0.1
               Nrefl 119385   1320   7673
             Nunique  15260    208   1018
--------------------------------------------------------------------------------
15 range: 271 -> 720
      Low resolution  29.28  29.28   2.95
     High resolution   2.88  12.86   2.88
              Rmerge  0.198  0.113  1.015
                Rpim  0.121  0.067  0.621
             I/sigma   6.70  12.70   1.40
        Completeness   99.1   91.3   95.7
        Multiplicity    6.6    5.4    6.4
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.3   96.3   93.7
  Anom. Multiplicity    3.5    4.0    3.4
   Anom. Correlation    0.0    0.2   -0.2
               Nrefl  88546    960   6006
             Nunique  13467    177    941
--------------------------------------------------------------------------------
16 range: 91 -> 720
      Low resolution  29.23  29.23   2.67
     High resolution   2.61  11.65   2.61
              Rmerge  0.210  0.110  1.112
                Rpim  0.105  0.054  0.560
             I/sigma   7.70  16.20   1.50
        Completeness   99.1   94.0   88.3
        Multiplicity    9.2    7.4    8.6
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   98.9   97.4   85.7
  Anom. Multiplicity    4.9    5.2    4.6
   Anom. Correlation   -0.0    0.1   -0.1
               Nrefl 164989   1810   9876
             Nunique  17945    243   1143
--------------------------------------------------------------------------------
17 range: 1 -> 720
      Low resolution  29.20  29.20   2.62
     High resolution   2.55  11.41   2.55
              Rmerge  0.214  0.116  0.963
                Rpim  0.099  0.052  0.472
             I/sigma   8.30  17.10   1.70
        Completeness   99.1   94.4   88.0
        Multiplicity   10.4    8.4    8.9
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   98.8   97.6   84.6
  Anom. Multiplicity    5.6    5.9    4.7
   Anom. Correlation   -0.1    0.0   -0.2
               Nrefl 198185   2177  10706
             Nunique  19004    260   1209
--------------------------------------------------------------------------------
18 range: 91 -> 810
      Low resolution  29.23  29.23   2.82
     High resolution   2.75  12.28   2.75
              Rmerge  0.220  0.114  1.126
                Rpim  0.102  0.052  0.523
             I/sigma   8.50  16.90   1.60
        Completeness   99.3   93.0   91.4
        Multiplicity   10.3    8.3    9.9
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.1   96.9   88.5
  Anom. Multiplicity    5.6    5.9    5.3
   Anom. Correlation   -0.0    0.4   -0.2
               Nrefl 159456   1730  10081
             Nunique  15432    209   1023
--------------------------------------------------------------------------------
19 range: 181 -> 810
      Low resolution  29.23  29.23   2.83
     High resolution   2.76  12.33   2.76
              Rmerge  0.224  0.110  1.345
                Rpim  0.112  0.054  0.673
             I/sigma   7.60  15.80   1.30
        Completeness   99.5   93.0   94.3
        Multiplicity    9.1    7.3    8.7
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.3   96.8   90.8
  Anom. Multiplicity    4.9    5.2    4.7
   Anom. Correlation   -0.0    0.6   -0.1
               Nrefl 138530   1527   9068
             Nunique  15287    208   1047
--------------------------------------------------------------------------------
20 range: 271 -> 810
      Low resolution  29.29  29.29   2.95
     High resolution   2.87  12.84   2.87
              Rmerge  0.226  0.111  1.321
                Rpim  0.122  0.059  0.721
             I/sigma   6.90  13.80   1.20
        Completeness   98.9   91.3   93.0
        Multiplicity    7.8    6.5    7.5
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.0   96.3   89.4
  Anom. Multiplicity    4.2    4.8    4.1
   Anom. Correlation   -0.1    0.6   -0.1
               Nrefl 105824   1150   6920
             Nunique  13495    178    924
--------------------------------------------------------------------------------
Merging point group: P 4 2 2
Unit cell:  81.50  81.50 167.05  90.00  90.00  90.00
Processing took 00h 21m 53s (1313 s)
kbadalian@cpu-009:~/nfdp$ fast_dp_gui
