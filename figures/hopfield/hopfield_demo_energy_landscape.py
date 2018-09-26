"""hopfield_demo_energy_landscape.py: 

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
import hopfield_demo

def compute_energe( frame ):
    frame = (1+frame)/2.0
    return np.mean( frame )

def run(i, ax):
    print( "[INFO ] Running for %d" % i  )
    stored, clue, states = hopfield_demo.main( plot = False )
    traj = [ compute_energe(x) for x  in states ]
    ax.plot( traj[:3], 'o-' )

def main( ):
    plt.figure()
    ax = plt.subplot( 111 )
    for i in range(100):
        run(i, ax)

    plt.savefig( 'figures/energy_landscape.png' )

if __name__ == '__main__':
    main()
