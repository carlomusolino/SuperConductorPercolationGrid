#!/usr/local/bin/python

##-----------------------------------------
#
# Script for Superconduction experiment simulation
# determine the average stechiometric coefficient for O
# YBCO_{7-x}
#
##-----------------------------------------

import numpy as np
from matplotlib import pyplot as plt

import sys

sys.path.append("/Users/carlomusolino/code/pyclust")

import pyclust as plc
from grid import *

xmax = .67
#means = np.linspace(0,0.65,5)
sigmas = np.linspace(0.01,0.1,3)

# Initialize grid (class in grid.py)
# Start temperature T = 90K

m = 0
#ns = np.arange(10,30,10)

ns = [90]

for i in range(5):
    for n in ns:
        for s in sigmas:
            T = 87
            G = Grid(n,n,T,mu=m,sigma=s)
            while not G.isSC:
                T -= 0.5
                G.updateT(T)
                G.updateR()
            f = open("tVsx.txt","a")
            f.write(str(m)+"   "+str(s)+"   "+str(T)+"    "+str(n)+"\n")
            f.close()
    
