import json
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer


f_json = json.load(open('pizza-train.json'))
request_text = []
y = []

# Get the requests and the receives from the file
for item in f_json:
    request_text.append(item['request_text'])
    y.append(item['requester_received_pizza'])

# Initialize the "CountVectorizer" object, which is scikit-learn's bag of words tool.
vectorizer = CountVectorizer(min_df=1, lowercase=True, stop_words='english')

# fit_transform() does two functions:
# Fits the model and learns the vocabulary;
# Transforms our training data into feature vectors;
bag_of_words = vectorizer.fit_transform(request_text)

# Convert the result to an numpy array
bag_of_words = bag_of_words.toarray()

# Shape of the bag
bag_of_words_shape = bag_of_words.shape
print 'Shape of the bag = %s' % (bag_of_words_shape,)

# The bag_of_words as a vocabulary
vocab = vectorizer.get_feature_names()
print 'Vocabulary = %s' % vocab

x_train, x_test, y_train, y_test = train_test_split(bag_of_words, y, test_size=0.10)

alg = linear_model.LogisticRegression()
alg.fit(x_train, y_train)
test_score = alg.score(x_test, y_test)
print test_score