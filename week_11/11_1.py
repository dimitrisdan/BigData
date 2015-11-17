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

forest = RandomForestClassifier(n_estimators = 50)

forest.fit(bow.tocsr()[:8301],topic[:8301])

pred = forest.predict(bow.tocsr()[8301:])

result = pred == np.array(topic[8301:])

print np.sum(result)/len(result)


