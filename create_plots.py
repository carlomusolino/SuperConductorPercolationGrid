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

data = np.loadtxt("tVsx.txt")

mu = data[:,0]
sigma = data[:,1]
Tc = data[:,2]
N = data[:,3]

#N_vals = np.unique(N)
N_vals = [10,30]


fig,ax = plt.subplots()

for n in N_vals:
    t = []
    sigma_n = sigma[N==n]; T_n = Tc[N==n]
    for s in sigma_n:
        t.append(np.average(T_n[sigma_n==s]))
    ax.plot(sigma_n,t,'o')

ax.set_xlabel(r"$\sigma$")
ax.set_ylabel(r"$T_c$ [K]")
ax.legend([r"N=10",r"N=30"])
fig.show()
fig.savefig("plots.png")
