Run FastDP as you normal would, but using the command fast_dp_pro instead of fast_dp.  It will now output up to 20 results based on the best rMerge values with completenesses of over 97.
To view the rest of the data, and graphs, run fast_dp_gui in the same directory you ran FastDP.

kbadalian@cpu-009:~/testdata$ fast_dp_pro KNA004_C5_350_master.h5 -j 16 -k 40
Fast_DP installed in: /home/kbadalian/fast_dp_pro
Starting image: KNA004_C5_350_master.h5
Reading KNA004_C5_350_master.h5 took 2.29s
Number of jobs: 16
Number of cores: 40
Processing images: 1 -> 900
Phi range: 0.00 -> 180.00
Template: KNA004_C5_350_??????.h5
Wavelength: 0.97913
Working in: /home/kbadalian/testdata
All autoindexing results:
Lattice      a      b      c  alpha   beta  gamma
     tP  81.20  81.20 166.50  90.00  90.00  90.00
     oC 114.90 114.90 166.50  90.00  90.00  90.00
     oP  81.20  81.20 166.50  90.00  90.00  90.00
     mC 114.90 114.90 166.50  90.00  90.10  90.00
     mP  81.20  81.20 166.50  90.00  90.10  90.00
     aP  81.20  81.20 166.50  90.10  90.10  90.00
Mosaic spread: 0.10 < 0.13 < 0.18
Happy with sg# 89
 81.35  81.35 166.70  90.00  90.00  90.00
--------------------------------------------------------------------------------
Best range: 1 -> 270
      Low resolution  29.17  29.17   2.27
     High resolution   2.21   9.88   2.21
              Rmerge  0.117  0.070  0.641
                Rpim  0.089  0.055  0.503
             I/sigma   6.60  15.10   1.50
        Completeness   99.1   96.0   91.6
        Multiplicity    4.0    3.4    3.8
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   93.6   98.5   83.5
  Anom. Multiplicity    2.0    2.0    2.0
   Anom. Correlation   -0.0   -0.0   -0.0
               Nrefl 113858   1307   7386
             Nunique  28795    387   1931
--------------------------------------------------------------------------------
2 range: 181 -> 450
      Low resolution  29.18  29.18   2.57
     High resolution   2.51  11.21   2.51
              Rmerge  0.137  0.083  0.650
                Rpim  0.102  0.062  0.491
             I/sigma   5.80  12.00   1.30
        Completeness   97.9   88.9   90.4
        Multiplicity    4.0    3.5    3.6
              CC 1/2    1.0    1.0    0.6
  Anom. Completeness   93.0   89.3   81.3
  Anom. Multiplicity    2.1    2.1    2.0
   Anom. Correlation    0.0    0.3    0.0
               Nrefl  79585    898   4735
             Nunique  19668    253   1313
--------------------------------------------------------------------------------
3 range: 1 -> 360
      Low resolution  29.17  29.17   2.32
     High resolution   2.27  10.13   2.27
              Rmerge  0.138  0.087  0.684
                Rpim  0.091  0.056  0.476
             I/sigma   7.00  15.30   1.70
        Completeness   98.9   95.8   87.6
        Multiplicity    5.3    4.5    4.9
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   96.6   98.4   78.9
  Anom. Multiplicity    2.7    2.7    2.7
   Anom. Correlation    0.0   -0.0   -0.0
               Nrefl 140315   1602   8380
             Nunique  26722    359   1698
--------------------------------------------------------------------------------
4 range: 271 -> 450
      Low resolution  28.93  28.93   2.75
     High resolution   2.68  11.98   2.68
              Rmerge  0.139  0.083  0.559
                Rpim  0.127  0.078  0.507
             I/sigma   4.60   8.50   1.30
        Completeness   97.2   86.1   89.6
        Multiplicity    2.7    2.5    2.7
              CC 1/2    1.0    1.0    0.6
  Anom. Completeness   76.8   87.9   68.4
  Anom. Multiplicity    1.2    1.6    1.5
   Anom. Correlation    0.0    0.6   -0.1
               Nrefl  43869    494   2961
             Nunique  16004    194   1090
--------------------------------------------------------------------------------
5 range: 91 -> 450
      Low resolution  29.20  29.20   2.49
     High resolution   2.43  10.86   2.43
              Rmerge  0.147  0.093  0.721
                Rpim  0.097  0.059  0.484
             I/sigma   6.60  13.80   1.40
        Completeness   98.2   91.3   89.0
        Multiplicity    5.3    4.6    4.6
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   94.6   93.2   76.8
  Anom. Multiplicity    2.7    2.9    2.5
   Anom. Correlation    0.0    0.3   -0.1
               Nrefl 115576   1316   6529
             Nunique  21692    286   1418
--------------------------------------------------------------------------------
6 range: 271 -> 540
      Low resolution  29.23  29.23   2.80
     High resolution   2.73  12.22   2.73
              Rmerge  0.152  0.088  0.730
                Rpim  0.126  0.076  0.599
             I/sigma   5.70  10.10   1.40
        Completeness   98.9   92.5   92.8
        Multiplicity    4.0    3.4    3.9
              CC 1/2    1.0    1.0    0.6
  Anom. Completeness   95.1   96.9   83.3
  Anom. Multiplicity    2.1    2.4    2.1
   Anom. Correlation    0.0    0.4   -0.1
               Nrefl  62231    693   4094
             Nunique  15498    206   1053
--------------------------------------------------------------------------------
7 range: 181 -> 540
      Low resolution  29.19  29.19   2.65
     High resolution   2.59  11.57   2.59
              Rmerge  0.154  0.094  0.775
                Rpim  0.108  0.067  0.547
             I/sigma   6.70  12.90   1.40
        Completeness   99.1   93.8   90.2
        Multiplicity    5.3    4.3    5.1
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.3   97.5   84.5
  Anom. Multiplicity    2.8    2.8    2.7
   Anom. Correlation   -0.0    0.3   -0.0
               Nrefl  97322   1067   6149
             Nunique  18253    246   1217
--------------------------------------------------------------------------------
8 range: 1 -> 450
      Low resolution  29.18  29.18   2.39
     High resolution   2.33  10.41   2.33
              Rmerge  0.160  0.101  0.744
                Rpim  0.095  0.058  0.451
             I/sigma   7.20  15.40   1.70
        Completeness   99.3   95.5   91.1
        Multiplicity    6.5    5.5    6.0
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.0   98.2   82.6
  Anom. Multiplicity    3.3    3.5    3.2
   Anom. Correlation   -0.0   -0.1   -0.1
               Nrefl 162210   1841   9885
             Nunique  24829    335   1635
--------------------------------------------------------------------------------
9 range: 91 -> 540
      Low resolution  29.21  29.21   2.56
     High resolution   2.50  11.18   2.50
              Rmerge  0.162  0.099  0.754
                Rpim  0.099  0.059  0.473
             I/sigma   7.30  14.70   1.60
        Completeness   99.2   94.5   90.6
        Multiplicity    6.6    5.4    5.9
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.7   97.8   85.6
  Anom. Multiplicity    3.5    3.6    3.1
   Anom. Correlation   -0.1    0.2   -0.1
               Nrefl 133886   1511   7906
             Nunique  20243    278   1339
--------------------------------------------------------------------------------
10 range: 271 -> 630
      Low resolution  29.27  29.27   2.86
     High resolution   2.79  12.46   2.79
              Rmerge  0.173  0.104  0.832
                Rpim  0.122  0.071  0.583
             I/sigma   6.30  11.50   1.50
        Completeness   99.1   92.1   94.6
        Multiplicity    5.3    4.4    5.2
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.8   96.7   91.7
  Anom. Multiplicity    2.8    3.2    2.8
   Anom. Correlation   -0.0    0.2   -0.1
               Nrefl  78377    860   5344
             Nunique  14729    195   1024
--------------------------------------------------------------------------------
11 range: 1 -> 540
      Low resolution  29.18  29.18   2.45
     High resolution   2.39  10.68   2.39
              Rmerge  0.175  0.107  0.809
                Rpim  0.095  0.056  0.468
             I/sigma   7.60  16.10   1.70
        Completeness   99.3   95.4   92.0
        Multiplicity    7.8    6.5    6.6
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   98.6   98.1   84.2
  Anom. Multiplicity    4.0    4.3    3.5
   Anom. Correlation   -0.1   -0.1   -0.2
               Nrefl 180708   2048  10211
             Nunique  23096    316   1543
--------------------------------------------------------------------------------
12 range: 181 -> 630
      Low resolution  29.21  29.21   2.70
     High resolution   2.63  11.75   2.63
              Rmerge  0.176  0.106  0.943
                Rpim  0.109  0.065  0.577
             I/sigma   7.10  14.10   1.60
        Completeness   99.3   93.7   91.4
        Multiplicity    6.6    5.4    6.4
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.1   97.3   88.5
  Anom. Multiplicity    3.5    3.6    3.4
   Anom. Correlation   -0.0    0.2   -0.1
               Nrefl 115929   1254   7359
             Nunique  17486    233   1146
--------------------------------------------------------------------------------
13 range: 91 -> 630
      Low resolution  29.22  29.22   2.65
     High resolution   2.58  11.54   2.58
              Rmerge  0.179  0.110  0.865
                Rpim  0.099  0.059  0.484
             I/sigma   7.90  15.70   1.70
        Completeness   99.4   94.2   92.6
        Multiplicity    7.9    6.4    7.3
              CC 1/2    1.0    1.0    0.9
  Anom. Completeness   99.2   97.5   89.9
  Anom. Multiplicity    4.2    4.4    3.9
   Anom. Correlation   -0.0    0.1   -0.1
               Nrefl 146890   1605   9151
             Nunique  18511    251   1247
--------------------------------------------------------------------------------
14 range: 1 -> 630
      Low resolution  29.19  29.19   2.52
     High resolution   2.46  10.99   2.46
              Rmerge  0.192  0.111  0.844
                Rpim  0.096  0.054  0.448
             I/sigma   8.10  16.80   1.90
        Completeness   99.4   95.0   92.5
        Multiplicity    9.2    7.4    8.0
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.2   97.9   89.9
  Anom. Multiplicity    4.8    5.0    4.2
   Anom. Correlation   -0.0    0.1   -0.2
               Nrefl 194640   2166  11339
             Nunique  21248    292   1420
--------------------------------------------------------------------------------
15 range: 181 -> 720
      Low resolution  29.24  29.24   2.80
     High resolution   2.73  12.22   2.73
              Rmerge  0.196  0.105  1.087
                Rpim  0.108  0.057  0.597
             I/sigma   7.60  15.00   1.50
        Completeness   99.5   93.2   94.6
        Multiplicity    7.8    6.3    7.6
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.2   96.9   90.6
  Anom. Multiplicity    4.2    4.4    4.1
   Anom. Correlation   -0.0    0.4   -0.1
               Nrefl 123123   1353   8131
             Nunique  15707    214   1070
--------------------------------------------------------------------------------
16 range: 271 -> 720
      Low resolution  29.29  29.29   2.91
     High resolution   2.84  12.69   2.84
              Rmerge  0.198  0.110  1.026
                Rpim  0.121  0.065  0.625
             I/sigma   6.70  12.90   1.50
        Completeness   99.2   91.7   96.6
        Multiplicity    6.6    5.4    6.4
              CC 1/2    1.0    1.0    0.7
  Anom. Completeness   99.2   96.6   92.5
  Anom. Multiplicity    3.5    4.0    3.4
   Anom. Correlation    0.0    0.4   -0.1
               Nrefl  92236   1012   6353
             Nunique  14010    186    994
--------------------------------------------------------------------------------
17 range: 91 -> 720
      Low resolution  29.24  29.24   2.65
     High resolution   2.58  11.54   2.58
              Rmerge  0.208  0.110  1.115
                Rpim  0.104  0.054  0.566
             I/sigma   7.70  16.40   1.50
        Completeness   99.5   94.2   93.7
        Multiplicity    9.2    7.4    8.5
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.3   97.5   90.7
  Anom. Multiplicity    4.9    5.2    4.6
   Anom. Correlation   -0.0    0.1   -0.1
               Nrefl 170266   1862  10769
             Nunique  18523    251   1261
--------------------------------------------------------------------------------
18 range: 1 -> 720
      Low resolution  29.20  29.20   2.56
     High resolution   2.50  11.17   2.50
              Rmerge  0.214  0.113  0.959
                Rpim  0.099  0.050  0.470
             I/sigma   8.10  17.40   1.80
        Completeness   99.5   94.8   93.8
        Multiplicity   10.4    8.4    9.1
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.2   97.8   90.0
  Anom. Multiplicity    5.5    5.8    4.9
   Anom. Correlation   -0.0    0.4   -0.1
               Nrefl 211450   2354  12636
             Nunique  20300    279   1385
--------------------------------------------------------------------------------
19 range: 181 -> 810
      Low resolution  29.26  29.26   2.86
     High resolution   2.78  12.45   2.78
              Rmerge  0.216  0.109  1.205
                Rpim  0.108  0.054  0.600
             I/sigma   7.90  15.90   1.60
        Completeness   99.6   92.8   95.7
        Multiplicity    9.1    7.3    9.0
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.5   96.8   93.4
  Anom. Multiplicity    4.9    5.2    4.8
   Anom. Correlation   -0.0    0.3   -0.2
               Nrefl 135395   1494   9244
             Nunique  14895    204   1031
--------------------------------------------------------------------------------
20 range: 271 -> 810
      Low resolution  29.30  29.30   2.97
     High resolution   2.90  12.96   2.90
              Rmerge  0.216  0.109  1.210
                Rpim  0.117  0.058  0.657
             I/sigma   7.20  13.90   1.50
        Completeness   99.2   91.1   96.9
        Multiplicity    7.9    6.4    7.6
              CC 1/2    1.0    1.0    0.8
  Anom. Completeness   99.3   96.2   93.1
  Anom. Multiplicity    4.2    4.8    4.1
   Anom. Correlation   -0.0    0.4   -0.1
               Nrefl 103560   1098   7001
             Nunique  13179    172    919
--------------------------------------------------------------------------------
Merging point group: P 4 2 2
Unit cell:  81.50  81.50 167.05  90.00  90.00  90.00
Processing took 00h 21m 04s (1264 s)

kbadalian@cpu-008:~/testdata$ fast_dp_gui
