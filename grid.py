##--------------------------------
# Here we define the grid class
# that will hold all sensible info
##---------------------------------

import copy
import sys
import numpy as np
from matplotlib import pyplot as plt

sys.path.append("/Users/carlomusolino/code/pyclust")

import pyclust as pcl


class Grid:

    def __init__(self,n,m,Temp,mu=0,sigma=0.3,distrtype="Gauss"):
        self.T = Temp # current temperature, later to be steered
        self.R = []
        self.isSC = False
        if distrtype == "Gauss":
            self.X = np.random.normal(mu,sigma,size=[n,m])
        else:
            self.X = random.uniform(0,0.67,size=[n,m])
        self.updateR()

        
    def updateT(self,T):
        self.T = T
        self.updateR()
        return

        
    def updateR(self,T=None):
        if T is None: T=self.T
        self.R = np.zeros(self.X.shape)
        self.isTrans()
        self.isSuperC()
        return
    

    def isTrans(self,T=None):
        if T is None: T=self.T
        Tc = -601.1986*self.X**3+580.6749*self.X**2-225.7929*self.X+85.775*np.ones(self.X.shape)
        m = Tc > np.ones(self.X.shape)*T
        for i in range(self.X.shape[0]):
            for j in range(self.X.shape[1]):
                if m[i,j]: self.R[i,j] = 1
        return
    
    def isSuperC(self):
        self.isSC = pcl.isPerc(self.R)
        return

    def visualize(self):
        n,m = self.R.shape
       # X = copy.deepcopy(self.X)
       # for i in range(n):
       #     for j in range(m):
       #         if self.R[i,j]: X[i,j] = 0
        fig,ax = plt.subplots()
        ax.imshow(self.X)
        ax.grid(which='major',axis='both',color='k',linewidth=2)
        ax.set_xticks(np.arange(-.5,m,1))
        ax.set_yticks(np.arange(-.5,n,1))
        ax.set_title(r"Grid at T=%2.1fK" %(self.T))
        fig1, ax1 = plt.subplots()
        ax1.imshow(self.R)
        ax1.grid(which='major',axis='both',color='k',linewidth=2)
        ax1.set_xticks(np.arange(-.5,m,1))
        ax1.set_yticks(np.arange(-.5,n,1))
        ax1.set_title(r"Grid at T=%2.1fK" %(self.T))
