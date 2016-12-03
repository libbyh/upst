from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

bible = open("religious-texts/King James Bible.txt").read()
quran = open("religious-texts/Quran.txt").read()

vectorizer = TfidfVectorizer() # read the docs on this, you can do a lot, pass in your own tokenizer, easily do n-grams, etc.
tdm = vectorizer.fit_transform([bible, quran])
# this is a matrix where each column represents a word and each row represents a document

feature_names = np.array(vectorizer.get_feature_names())
#this gets us access to the vocabulary

top_bible_scores = np.argsort(tdm.A[0])[-5:]
# argsort returns an array with the indices that would sort an array,
# i.e., np.argsort([2, 6, 4]) would return [0, 2, 1]
top_quran_scores = np.argsort(tdm.A[1])[-5:]

top_bible_words = feature_names[top_bible_scores]

print(top_bible_words)
print(tdm.A[0][top_bible_scores])