#! /usr/bin/env python

import nltk
import sys

# First, let's get input from the user:

print("Enter the word for which you would like to see similar words:", end=' ')
word = input()

# Then we need to transform the base text using a series of steps.
# Please note this could be one line:

thefile = open('mdg.txt')
rawtext = thefile.read()
tokens = nltk.word_tokenize(rawtext)
text = nltk.Text(tokens)

# Now we can actually look at a word:

similarwords = text.similar(word)

print(similarwords)