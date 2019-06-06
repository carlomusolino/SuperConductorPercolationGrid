#!/usr/bin/env python3

import numpy as np
import copy
from matplotlib import pyplot as plt

PackageDescription = """

Definition of the Cluster class and related functions. 


Only defined function is now FindBinClust( bin_array ) 

"""
class Cluster:
# Cluster has a source array and an initial element, its method allow updating of the cluster. 
    def __init__(self,arr,ind):
        i,j = ind
        n,m = arr.shape
        #source and empty cluster initialization
        self.shape=arr.shape
        self.clust=np.zeros(arr.shape)
        self.src = arr
        #self.isPerc = False
        self.isPercolated()
        #initialize neighbors of first element and things we shouldn't bother checking
        self.neighbors = [[i,j]]
        self.checked = [[i,j]]
        for i in range(n):
            self.checked.append([i,-1])
            self.checked.append([i,m])
            for j in range(m):
                self.checked.append([-1,j])
                self.checked.append([n,j])
                
        return

    def push(self,ind):
        i,j = ind
        self.clust[i,j] = 1
        self.src[i,j] = 0
        self.pull(ind)
        isToInclude = self.__isToCheck(ind)
        if isToInclude[0,0]: self.neighbors.append([i-1,j])
        if isToInclude[1,0]: self.neighbors.append([i,j-1])
        if isToInclude[0,1]: self.neighbors.append([i+1,j])
        if isToInclude[1,1]: self.neighbors.append([i,j+1])
        #self.neighbors=np.unique(self.neighbors)
        return
    
    def pull(self,ind):
        i,j = ind
        self.checked.append([i,j])
        self.neighbors.remove([i,j])

    def __isBound(self,ind): #unused
        n,m = self.src.shape
        OUT = np.array([[True,True],[True,True]])
    
        if (ind[0] == 0)  : OUT[0,0] = False
        if (ind[1] == 0)  : OUT[1,0] = False
        if (ind[0] == n-1): OUT[0,1] = False
        if (ind[1] == m-1): OUT[1,1] = False
        
        return OUT
   
    def __isToCheck(self,ind):
        i,j = ind
        OUT = np.array([ [True, True], [True, True] ])

        if ( [i-1,j] in self.checked ): OUT[0,0] = False
        if ( [i,j-1] in self.checked ): OUT[1,0] = False
        if ( [i+1,j] in self.checked ): OUT[0,1] = False
        if ( [i,j+1] in self.checked ): OUT[1,1] = False
        
        return OUT
    
    def isPercolated(self):
        n,m = self.shape
        a = np.sum(self.clust[:,0])
        b = np.sum(self.clust[:,m-1])
        if a and b:
            self.isPerc = True
            return True
        else:
            self.isPerc = False
            return False

class ColorMaps:
    pass
ColorMaps.items = {
    'Black' : [0,0,0],
    'White' : [255,255,255],
    'Red' : [255, 0, 0],
    'Green' : [0, 255, 0],
    'Blue' : [0,0,255],
}
    



    
#############################################################################################                               
####
####                              M A I N
####
#############################################################################################

def isPerc(arr):
    clusts = FindBinClust(arr)
    for c in clusts:
        if c.isPercolated():
            return True
        else:
            pass
    return False
            

def FindBinClust(original_arr):
    """
    
    Find clusters in a binary matrix i.e. one whose elements are ones or zeros
    
    FindBinClust( [ [1, 1, 0] 
                    [1, 0, 0] 
                    [0, 0, 1] ] )
    
    --->  [  c_1  , c_2 ]

    --->  c_1.clust = [ [1, 1, 0] 
                        [1, 0, 0] 
                        [0, 0, 0] ] 

    --->  c_2.clust = [ [0, 0, 0]
                        [0, 0, 0]
                        [0, 0, 1] ]

    """
    arr = copy.deepcopy(original_arr)
    n, m = arr.shape
    checked = np.zeros([n,m])
    clusts = []
    
    for i in range(n):
        for j in range(m):
            if arr[i,j]:
                c = Cluster(arr,[i,j])
                c.push([i,j])
                while (len(c.neighbors) > 0):
                    for ind in c.neighbors:
                        if arr[ind[0],ind[1]] : c.push([ind[0],ind[1]])
                        else : c.pull([ind[0],ind[1]])
                clusts.append(c)
    return clusts
                
#def FindImgClust(img,requested_colors='Black'):
    
#    '''
#    Finds coherently coloured parts of an image and returns them as cluster objects

#    Depends on FindBinClust. To produce bin matrix color_map is used and all pixels of that color are returned. If colormap is a list returns a list of objects.

#    '''
    #parse color argument
#    for color_map in requested_colors:
#    if color_map in ColorMaps.items:
#        color_name = color_map
#        color_map = ColorMaps.items[color_map]
#    elif color_map in ColorMaps.items.values():
#        pass
#    elif type(color_map) is list and len(color_map) == 3:
#        try:
#            for i in range(3): int(color_map[i])
#        except:
#            raise(ValueError, "color_map must be one of the supported colors or an RGB value list")
        
#    #now color_map = [R, G, B]              
#    binSources = IM.ImgFindColor(img,color_map)
#    OUT = {}
#    for binSrc in binSources:
        
#        clusts = FindBinClust(binSrc)

#        OUT[]
    

