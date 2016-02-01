import nltk
from nltk import *
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import string
def word_feats(words):
    return dict([(word, True) for word in words])
negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')

negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]

negcutoff = len(negfeats)*1
poscutoff = len(posfeats)*1
 
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
raw = (open("data.txt").read())
for c in string.punctuation:
	raw=raw.replace(c,"")
text = word_tokenize(raw)
testfeats = word_feats(text)
testfeats1 = [((testfeats),'neg')]
print testfeats1[0]
print 'train on %d instances, test on %d instances' % (len(trainfeats), len(testfeats1))
classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats1)
