from __future__ import division

import mmh3
import numpy as np
from bitarray import bitarray
import re
import time


class FlajoletMartin():

    def __init__(self, noBuckets, noHashInBucket):

        self.noBuckets = noBuckets
        self.noHashInBucket = noHashInBucket

        self.bitmap = []

        # Generate seeds for hash functions
        self.seeds = np.random.choice(1000000, size=(noBuckets,noHashInBucket), replace=False)


        # Create noBuckets x noHashInBucket empty bitarrays
        # A bit array can be accesed by bitmap[Bucket number][Hash number in bucket]
        for bucket in xrange(noBuckets):
            newBucket = []
            for hash in xrange(noHashInBucket):

                newBucket.append((33) * bitarray('0'))

            self.bitmap.append(newBucket)

    def trailing_zeroes(self, num):
        """Counts the number of trailing 0 bits in num."""
        if num == 0:
            return 32 # Assumes 32 bit integer inputs!
        p = 0
        while (num >> p) & 1 == 0:
            p += 1
        return p

    # Finding
    def first_zero(self,bitarr):

        index = 0

        while (1 & bitarr[index]) == 1:
            index += 1

        return index


    def process(self,element):


        for bucketNo in xrange(self.noBuckets):
            for hashNo in xrange(self.noHashInBucket):

                #Hash element using seed from self.seeds
                hashedElement = mmh3.hash(element, self.seeds[bucketNo,hashNo]) % 4294967295

                #Find number of trailing zeroes
                no = self.trailing_zeroes(hashedElement)

                #set bit to one
                self.bitmap[bucketNo][hashNo][no] = 1


    def give_estimate(self):

        medians = []

        for group in self.bitmap:

            cardinalitylist = []

            for bitmaps in group:

                #Find cardinality for bitarray in group
                cardinalitylist.append((2 ** self.first_zero(bitmaps)) / 0.77351)

            #Calculate median in group and add to list "medians" that keep tab on medians of all groups
            medians.append(np.median(cardinalitylist))

        #Calculate mean of K groups median
        return np.average(medians)



# ========================================== #
#                   MAIN                     #
# ========================================== #

# Set up timing mechanism
startTime = time.time()

#open shakespear file
shakespeare = open('shakespeare.txt')

# Create FlajoletMartin with 100 groups with 10 hash function in each group
u = FlajoletMartin(100,10)

#Read the shakesper file
for line in shakespeare:

   #Loop through all words, remove punctuation and proccess word in FlajoletMartin
   for word in line.split():
       word = re.sub(r'[^\w\s]','',word.lower())
       u.process(word)

print '\n-------------------------------------'
print 'Flajolet-Martin Estimation\n'
print u.give_estimate()
print '--------------------------------------\n'
print 'Execution Time'
print("--- %s seconds ---" % (time.time() - startTime))
