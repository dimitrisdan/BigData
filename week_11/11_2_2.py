import pickle
import numpy as np
import scipy
from collections import Counter

hasharrays = pickle.load( open( "save.p", "rb" ) )
matrix = np.matrix(hasharrays)

print matrix.shape[1]

bucdict = dict()
allSig = []

for index in xrange(matrix.shape[1]):
    bucket = np.array_str(np.array(matrix[:,index]).flatten())
    if bucket in bucdict:
         # append the new number to the existing array at this slot
         bucdict[bucket].append(index)
    else:
    #     # create a new array in this slot
         bucdict[bucket] = [index]

    allSig.append(bucket)

#print bucdict
print Counter(allSig).most_common()

col = np.array(matrix[:,0])

print np.array_str(col.flatten())

