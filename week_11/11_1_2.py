from __future__ import division

import mmh3
import numpy as np

print mmh3.hash("hahahahha") % 1000

import json
import os
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from scipy import sparse
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

bow = bow.transpose().toarray()
np.random.shuffle(bow)
bow = sparse.csc_matrix(bow)

print bow.shape
numFeatures = bow.shape[0]
numArticles = bow.shape[1]

print bow.getcol(0)

