# Preprocessing: Download the words package from nltk
# import nltk
# nltk.download()

import json
import re
from nltk.corpus import stopwords
import numpy as np
import os
import json
from collections import Counter
import pickle
import scipy
from scipy.sparse import csr_matrix

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

print body[3]

class BagOfWords:

    def __init__(self):

        self.words = set()
        self.doc_count = []


    def add_document(self,string):

        p = re.compile(ur'\b[a-zA-Z][a-zA-Z]+\b')

        #temp = re.sub("[^a-zA-Z ]", "", string)
        #preg_match_all($re, $str, $matches);

        regWords = re.findall(p, string.lower())
        split = tuple(regWords)
        self.words.update(split)
        self.doc_count.append(Counter(split))

    def get_bow(self):
        counter = 0
        features = np.array(sorted(list(self.words)))
        bowarray = []

        for doc in self.doc_count:
            counter +=1
            print counter

            # for word in self.words:
            #    doc.get(word,0)

            res = np.in1d(features,dict(doc).keys(),assume_unique=True)
            #print res
            bowarray.append(res)

        return bowarray

bow = BagOfWords()

for doc in body:
   bow.add_document(doc)

x = np.array(bow.get_bow())
x = csr_matrix(x)
pickle.dump( x, open( "bow.p", "wb" ) )
pickle.dump(body,open( "body.p", "wb" ))

