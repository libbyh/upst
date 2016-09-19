#! /usr/bin/env python

import nltk
import sys
from configparser import SafeConfigParser
import os

def concordance(textfile, word, lines = 25):
    textfile = open(textfile)
    rawtext = textfile.read()
    tokens = nltk.word_tokenize(rawtext)
    text = nltk.Text(tokens)

    # Now we can actually look at a word.
    # concordance returns a context window of 79 characters and 25 lines by default
    # if we want to see a diff number
    concordword = text.concordance(word, lines = lines)

    return concordword
    
def main():
    # Get file to use from settings.cfg:
    config = SafeConfigParser()
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, 'settings.cfg')
    config.read(config_file)

    textfile = config.get('files','full_text')

    # ask the user what word to use
    word = input("Which word's concordance do you want to see? ")
    lines = int(input("How many lines would you like to see? "))
    concordword = concordance(textfile, word, lines)
    print(concordword)

if __name__ == '__main__' :
    main()