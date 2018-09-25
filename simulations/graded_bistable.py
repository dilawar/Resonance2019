"""milti_stable_bistable.py: 
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

random.seed( 10 )

class Bistable( ):

    def __init__(self):
        self.pup = 0.01
        self.pdown = 0.01
        self.x = random.choice([0,1])
        self.xs = []

    def step( self ):
        self.xs.append( self.x )
        if self.x >= 0.8:
            if random.random() < self.pdown:
                self.x = random.uniform(0, 0.2)
            else:
                self.x = random.uniform(0.8, 1.0)
        elif self.x < 0.2:
            if random.random() < self.pup:
                self.x = random.uniform(0.8, 1.0)
            else:
                self.x = random.uniform(0, 0.2)
        else:
            pass

    def steps( self, N ):
        for i in range(N):
            self.step()

def main( ):
    a1 = Bistable( )
    a2 = Bistable( )
    a3 = Bistable( )
    a4 = Bistable( )
    a5 = Bistable( )
    N = 2000
    df = pd.DataFrame( )
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    for i, a in enumerate([a1, a2, a3, a4, a5]):
        a.steps( int(N) )
        df[ 'switch%i' % i] = a.xs

    df.to_csv( 'bistable_graded.csv', index = False )
    ax1.plot( a1.xs )
    ax2.plot( np.sum( [a2.xs, a3.xs, a4.xs, a5.xs], axis = 0) )
    plt.savefig( '%s.png' % __file__ )

if __name__ == '__main__':
    main()
