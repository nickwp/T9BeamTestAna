import numpy as np

ACT0L    = 0
ACT0R    = 1
ACT1L    = 2
ACT1R    = 3
ACT2L    = 4
ACT2R    = 5
ACT3L    = 6
ACT3R    = 7
TOF00    = 8
TOF01    = 9
TOF02    = 10
TOF03    = 11
TOF10    = 12
TOF11    = 13
TOF12    = 14
TOF13    = 15
Hole0    = 16
Hole1    = 17
PbGlass  = 18
ACT0     = np.s_[0:2]   # select both ACT 0 PMTs
ACT1     = np.s_[2:4]   # select both ACT 1 PMTs
ACT2     = np.s_[4:6]   # select both ACT 2 PMTs
ACT3     = np.s_[6:8]   # select both ACT 3 PMTs
ACT0and1 = np.s_[0:4]   # select ACT 0 and ACT 1
ACT2and3 = np.s_[4:8]   # select ACT 2 and ACT 3
TOF0     = np.s_[8:12]  # select all TOF 0
TOF1     = np.s_[12:16] # select all TOF 1
TOF0and1 = np.s_[8:16]  # select all TOF 0 and TOF 1