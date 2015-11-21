from __future__ import division
import numpy as np
import pickle

bow = pickle.load( open( "bow.p", "rb" ) )

bow = bow.transpose()

numFeatures = bow.shape[0]
numArticles = bow.shape[1]

permutations = []
hasharrays = []

for x in xrange(3):
    num = np.arange(numFeatures)
    np.random.shuffle(num)
    permutations.append(num)

for perm in permutations:

    hasharray = np.zeros(numArticles)

    count = 0;

    while 0 in hasharray and count < numFeatures:
        temp = bow.getrow(perm[count]).nonzero()[-1];  #geting indices in a row where value is 1
        temps = np.setdiff1d(temp,hasharray.nonzero()[-1]) # Get incdices
        hasharray[temps] = count + 1
        count += 1

    print hasharray

    hasharrays.append(hasharray)

pickle.dump( hasharrays, open( "save.p", "wb" ) )
