from __future__ import division
import scipy
import numpy as np
cimport numpy as np
from collections import Counter

def DBSCAN(D, float eps, int MinPts):
    cdef int C = 0

    UNCLASSIFIED = False
    NOISE = None

    cdef list index
    cdef list visited
    cdef list NeighborPts

    index = [UNCLASSIFIED] * D.shape[1]
    visited = [UNCLASSIFIED] * D.shape[1]

    cdef int p
    for p in xrange(D.shape[1]):
        if visited[p]:
            continue
        visited[p] = True

        NeighborPts = regionQuery(D,p, eps)

        if len(NeighborPts) < MinPts:
            index[p] = NOISE
        else:
            C += 1
            index[p] = C

            while NeighborPts:
                point = NeighborPts.pop(0)
                if not visited[point]:
                    visited[point] = True
                    NewNeighborPts = regionQuery(D,point,eps)
                    if len(NewNeighborPts) >= MinPts:
                        NeighborPts = NeighborPts + NewNeighborPts
                
                #If not member of cluster assign clster
                if not index[point]:
                    index[point] = C
    
    #return array where value corresponds to cluster
    #e.g index[3] = 4 means that point 3 is a member of cluster 4 
    return index

def regionQuery(D,int P,float eps):
    #Find m11 in matrix
    m11 = D[P].multiply(D).sum(axis=1)
    
    Old = D.sum(axis=1)

    #Jaccard Distance between every point in sparse matrix D and Point P 
    reg = (Old - m11 + Old[P] - m11)/(Old - m11 + Old[P] - m11 + m11)
    
    #Return index of points in Matrix D that has a jaccard distance 
    #bellow the threshold eps
    return list(np.where(reg <= eps)[0].A1)