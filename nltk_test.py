import nltk
from nltk import *
raw = file(open("data.txt").read())
tokens = word_tokenize(raw)
print tokens