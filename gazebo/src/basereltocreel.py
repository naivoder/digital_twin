import numpy as np
import math as m

'''
Row and Column are from 0-5 starting from the top left peg being (0,0)
brph must be a 4x4 matrix
brpH = Homogeneous matrix of the Base Relative to the Peg
'''
def basereltocreel(brpH,row,col):

    pegmatrix = [[[414.13,-258.31,1916.32,m.radians(14.11603)], [415.31,-553.42,1913.05,m.radians(-14.526)], [408.72,-1038.64,1917.07,m.radians(13.117)], [406.44,-1344.28,1915.74,m.radians(-14.526)], [406.44,-1829.50,1916.32,m.radians(13.117)], [411.43,-2136.87,1916.32,m.radians(-13.50)]],   #0
               [[414.13,-258.31,1586.12,m.radians(14.11603)], [415.31,-553.72,1585.85,m.radians(-14.526)], [408.72,-1038.94,1586.87,m.radians(13.117)], [413.04,-1344.28,1585.54,m.radians(-14.526)], [406.44,-1829.50,1586.12,m.radians(13.117)], [411.43,-2136.87,1586.98,m.radians(-13.50)]],    #1
               [[414.13,-258.31,1255.92,m.radians(14.11603)], [415.31,-554.02,1255.65,m.radians(-14.526)], [408.72,-1038.24,1256.67,m.radians(13.117)], [413.04,-1344.28,1255.34,m.radians(-14.526)], [406.44,-1829.50,1255.92,m.radians(13.117)], [411.43,-2136.87,1256.87,m.radians(-13.50)]],    #2
               [[458.58,-258.31,925.720,m.radians(14.11603)], [415.3,-554.32,925.45,m.radians(-14.526)],   [408.72,-1038.54,926.47,m.radians(13.117)],  [413.04,-1344.28,925.14,m.radians(-14.526)],  [406.44,-1829.50,925.72,m.radians(13.117)],  [411.43,-2136.87,596.38,m.radians(-13.50)]],     #3
               [[414.13,-258.31,595.520,m.radians(14.11603)], [415.3,-554.62,595.25,m.radians(-14.526)],   [408.72,-1039.84,596.27,m.radians(13.117)],  [413.04,-1344.28,594.94,m.radians(-14.526)],  [406.44,-1829.50,595.52,m.radians(13.117)],  [406.44,-2136.87,596.38,m.radians(-13.50)]],     #4
               [[414.13,-258.31,265.32,m.radians(14.11603)],  [415.3,-554.92,265.05,m.radians(-14.526)],   [408.71,-1040.14,266.07,m.radians(13.117)],  [413.04,-1344.28,264.74,m.radians(-14.526)],  [406.44,-1829.50,265.32,m.radians(13.117)],  [406.44,-2136.87,266.18,m.radians(-13.50)]]]     #5
    #           ^^^sets the position and rotation of each peg
    prcH = np.array([ [ m.cos(pegmatrix[row][col][3]), m.sin(pegmatrix[row][col][3]),      0    , pegmatrix[row][col][0]],
                      [-m.sin(pegmatrix[row][col][3]), m.cos(pegmatrix[row][col][3]),      0    , pegmatrix[row][col][1]],
                      [                0              ,               0              ,     1    , pegmatrix[row][col][2]],
                      [                0              ,               0              ,     0    ,            1          ]
                    ])
    #           ^^^Creates the Homogeneous matrix of the "Peg Relative to the Creel"->(prcH)
    return brpH*prcH
    
    
    
###########################################################################################
#using it
###########################################################################################
A = np.array([ [ .92, -.25, 0, 500],
                  [ .25, .95,  0, 500],
                  [  0 ,  0  , 1, -500],
                  [  0 ,  0  , 0, 1  ],
                ])
print('The base relative to the creel is:')
print (basereltocreel(A,2,1))
