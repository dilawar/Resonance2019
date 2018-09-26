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
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

def main():
    y = 1 if random.random() < 0.5 else 0
    res = [y]
    pup, pdown = 0.01, 0.01 
    tvec = [0]
    for i in range(1, 1000):
        tvec.append( i )
        if res[-1] > 0.8:
            if random.random() < pdown:
                res.append(0)
            else:
                res.append( random.uniform(0.8, 1.0) )
        else:
            if random.random() < pup:
                res.append(1)
            else:
                res.append( random.uniform(0, 0.2) )

    df = pd.DataFrame()
    df['steps'] = tvec
    df['state'] = res
    df.to_csv( 'data.csv', index = False )

    plt.plot( tvec, res )
    plt.savefig( 'res.png' )

        

if __name__ == '__main__':
    main()
