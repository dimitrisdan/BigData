from __future__ import division
import json
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from pprint import pprint

from sklearn.ensemble import RandomForestClassifier

topic = list()
body = list()

for file in os.listdir("Data"):
    with open("Data/" + file) as json_file:
        data = json.load(json_file)
        for file in data:
            if 'body' in file and 'topics' in file:

                if 'earn' in file['topics']:
                    topic.append(True)
                else:
                    topic.append(False)

                body.append(file['body'])

vectorizer = CountVectorizer(body,binary=True)
bow = vectorizer.fit_transform(body)

bow = bow.tocsr().transpose()

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
        temp = bow.getrow(perm[count]).nonzero()[-1];
        temps = np.setdiff1d(temp,hasharray.nonzero()[-1])
        hasharray[temps] = count + 1
        #print count
        count += 1

    print hasharray

    hasharrays.append(hasharray)


#permutations.append(np.arange(10))

#print x
#np.random.shuffle(x)
#print (x == x



# print bow.transpose().shape[0]
#
# arr = np.arange(9).reshape((3, 3))
# print arr
# np.random.shuffle(arr)
# print arr



# print bow.tocsr()[0]
#
# myarray = np.zeros(10)
# print np.isnan(myarray).any()
#
#
# index =
# print bow[0].nonzero()[-1]
# hasharray = np.zeros(numArticles)
# hasharray[bow.getrow(0).nonzero()[-1]] = 1
# #print (bow.tocsr()[0] == 0).toarray()
