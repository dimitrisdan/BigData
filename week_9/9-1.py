import string

# Path to shakespeare file
filename = ("/home/vagrant/data/cs100/lab1/shakespeare.txt")
lines = sc.textFile(filename)

# Read lines, filter words and compute the result
# Set to lowercase
# Remove punctuations
# Split lines into words
# Assign 1 occurunce to each of the words
# Count word occurances
words = lines.map(lambda text: text.lower()) \
             .map(lambda text: text.translate({ord(c): None for c in string.punctuation})) \
             .flatMap(lambda line: line.split()) \
             .map(lambda w: (w,1)) \
             .reduceByKey(lambda v1, v2: v1 + v2)

words.take(5)