#! /usr/bin/env python
import nltk
import sys, os
from configparser import SafeConfigParser

# First, let's get input from the user:
word = input("Enter the word for which you would like to see a dispersion graph: ")

# I can't get this to work for multiple words
# words = raw_input().split(",")


# Then we need to transform the base text using a series of steps.
# Get file to use from settings.cfg:
config = SafeConfigParser()
script_dir = os.path.dirname(__file__)
config_file = os.path.join(script_dir, 'settings.cfg')
config.read(config_file)

textfile = config.get('files','full_text')

thefile = open(textfile, 'r')
rawtext = thefile.read()
tokens = nltk.word_tokenize(rawtext)
text = nltk.Text(tokens)

# Now we can actually look at a word:

graphed = text.dispersion_plot([word])

# print(similarwords)