# Preprocessing: Download the words package from nltk
# import nltk
# nltk.download()

import json
import re
from nltk.corpus import stopwords
import numpy as np
import os
import json

topic = list()
body = list()

req_txt_clean = []
req_txt_words = []

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

# Get the requests from the file
for req_txt in body:

    # Remove any non-letter character(e.g. numbers)
    req_txt_only_letters = re.sub("[^a-zA-Z]", " ", req_txt)

    # Convert to lowercase
    req_txt_lower_case = req_txt_only_letters.lower()

    #print(req_txt_lower_case)

    # # Remove stopwords
    # stops = set(stopwords.words("english"))
    # req_txt_stopwords = []
    # for word in req_txt_lower_case.split():
    #     if not word in stops:
    #         req_txt_stopwords.append(word)
    #
    # # Join the words back into one string separated by space
    # req_txt_join = " ".join(req_txt_stopwords)

    # # Append the clean request to a list
    # req_txt_clean.append(req_txt_join)
    #
    # # Split into words
    # req_txt_words.extend(req_txt_join.split())

    req_txt_clean.append(req_txt_lower_case)
    req_txt_words.extend(req_txt_lower_case.split())

# Create a set with all the unique words from the file
vocabulary = sorted(set(req_txt_words))
no_unique_words = len(vocabulary)
no_requests = len(req_txt_clean)

print no_unique_words
print no_requests

# # Initialize the bag of words array with zeros
# bag_of_words = np.zeros((no_requests, no_unique_words), dtype=np.int).tolist()
#
# for i in xrange(0, no_requests):
#     words = req_txt_clean[i]
#     words = words.split()
#     for word in words:
#         if word in vocabulary:
#             bag_of_words[i][vocabulary.index(word)] += 1
#
# print len(bag_of_words)
# print len(bag_of_words[0])