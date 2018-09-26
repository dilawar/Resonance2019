"""main.py: 

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

import sys
import os
import math
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

def get_ca( t ):
    ca = 0.01
    if t > 15:
        return ca
    if t % 2 > 1:
        ca = 1 * (1 +  0.3 * random.gauss(0, 0.5))
    return ca

def leaky_integrate( xs, dt, tau ):
    val = [0.0]
    factor = 1e-3
    for x in xs:
        v = val[-1] + factor * x
        v -= v / tau    # decay
        val.append(v)
    return val[1:]

def main():
    dt = 0.01
    tvec = []
    ca = []
    df = pd.DataFrame()
    for t in np.arange( 0, 20.0, dt ):
        tvec.append(t )
        ca.append( get_ca( t ) )

    camkii0 = leaky_integrate( ca, dt, 1e9 )
    camkii1 = leaky_integrate( ca, dt, 1e3 )
    camkii2 = leaky_integrate( ca, dt, 2e2 )
    df['Time'] = tvec
    df['calcium'] = ca
    df['CaMKII0'] = camkii0
    df['CaMKII1'] = camkii1
    df['CaMKII2'] = camkii2

    ax = plt.subplot( 111 )
    ax.plot( tvec, ca , label = 'Ca')
    ax1 = ax.twinx()
    ax1.plot( tvec, camkii0, color = 'red' , label = 'CaMKII' )
    ax1.plot( tvec, camkii1, label = 'CaMKII' )
    ax1.plot( tvec, camkii2, label = 'CaMKII' )
    plt.savefig( '%s.png' % __file__ )

    df.to_csv( 'data.csv', index = False )

if __name__ == '__main__':
    main()
