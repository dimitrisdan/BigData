import mmh3
import re
import time
import string
from bitarray import bitarray


class Bloom:

    bit = (10**6) * bitarray('0') # Length of filter

    def __init__(self, numberofhash):

        Bloom.numberofhash = numberofhash
        Bloom.bit = (10**6) * bitarray('0')

    def add(self, string):

        # Hash the string
        hashlist = [mmh3.hash(string, seed=x) % 1000000 for x in xrange(Bloom.numberofhash)]

        for x in hashlist:
            Bloom.bit[x] = 1

    def count(self):

        # Count the zeros in the bitarray
        return Bloom.bit.count(False)

    def lookup(self, string):

        hashlist = [mmh3.hash(string, seed=x) % 1000000 for x in xrange(Bloom.numberofhash)]
        for x in hashlist:
            if not Bloom.bit[x]:
                return False
        return True

# ========================================== #
#                   MAIN                     #
# ========================================== #

# BLOOM FILTER METHOD

# Start counting time
start = time.time()

# A filter object,
# 3 is the number of performed hash functions
Bfilter = Bloom(3)

# Total words of shakespeare.txt
total_words = 0

# The words that will be matched in the bitarray
found_words = 0

found_word_set = set()

# Add the words of the dictionary to the Bfilter
f = open('dict')
for word in f.read().lower().split():
    Bfilter.add(word)

f.close()

# Read the words from the file and lookup in the Bfilter
f = open('shakespeare.txt')
for word in f.read().split():

    #remove punctuation and convert to lowercase
    word = re.sub(r'[^\w\s]', '', word.lower())

    total_words += 1
    if Bfilter.lookup(word):
        found_words += 1
        found_word_set.add(word)

f.close()

missing_words = total_words-found_words

stop = time.time()
execution_time = stop - start
print '\nBLOOM FILTER ALGORITHM'
print '---------------------------------------------------------'
# print 'Number of zeros in Bitarray: %s' % Bfilter.count()
print 'Total words of shakespeare.txt : %d' % total_words
print 'Possible matches between shakespeare.txt and dictionary: %d' % found_words
print 'Missing words : %d' % missing_words
print 'Execution time : %f !!' % execution_time
print '---------------------------------------------------------'

# ALTERNATIVE METHOD

start = time.time()
final_words = []
s = open('shakespeare.txt')
d = open('dict')

dict = d.read().lower().split()

# Iterate through every word in shakespeare.txt
for word in s.read().split():

    # To remove punctuations and convert to locercase
    word = re.sub(r'[^\w\s]', '', word.lower())
    total_words += 1
    if word in dict and word not in final_words:

            # If in dictionary, add to final_words
            final_words.append(word)

s.close()
d.close()

stop = time.time()
execution_time = stop - start

print '\nALTERNATIVE METHOD'
print '---------------------------------------------------------'
print "Distinct matching words between shakespeare.txt and dictionary: %d" % len(final_words)
print "Execution time: %f" % execution_time
print '---------------------------------------------------------'


# FIND

s = open('shakespeare.txt')
d = open('dict')

dict = d.read().lower().split()
not_there = []

for word in found_word_set:
    if word not in dict:
        not_there.append(word)

s.close()
d.close()

print '\nWORDS REPORTED TO BE IN DICTONARY BY BLOOM BUT ARE NOT THERE '
print '---------------------------------------------------------'
print sorted(not_there)
print '---------------------------------------------------------'
