from __future__ import division

import mmh3
import numpy as np


import json
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy import sparse
import re
from pprint import pprint
from scipy.sparse import csr_matrix


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

class featurehash:

    def __init__(self):

        self.hashed_document = []


    def add_document(self,string):

        hasharray = np.zeros(1000)
        p = re.compile(ur'\b[a-zA-Z][a-zA-Z]+\b')
        words = re.findall(p, string.lower())

        for word in words:
            index = mmh3.hash(word,seed=21) % 1000
            hasharray[index] = hasharray[index] + 1

        self.hashed_document.append(hasharray)

    def getMatrix(self):

        return csr_matrix(self.hashed_document)

ft = featurehash()

for doc in body:
   ft.add_document(doc)

bow = ft.getMatrix()
print bow.shape
forest = RandomForestClassifier(n_estimators = 50)

forest.fit(bow[:8301],topic[:8301])

pred = forest.predict(bow[8301:])

result = pred == np.array(topic[8301:])

print np.sum(result)/len(result)


