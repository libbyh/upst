#! /usr/bin/env python

import nltk
import sys
import argparse
from configparser import SafeConfigParser
import os
import sys

def concordance(textfile, word):
    textfile = open(textfile)
    rawtext = textfile.read()
    tokens = nltk.word_tokenize(rawtext.decode('utf-8'))
    text = nltk.Text(tokens)

    # Now we can actually look at a word:
    concordword = text.concordance(word)

    return concordword
    
def main():
    # Get file to use from settings.cfg:
    config = SafeConfigParser()
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, 'settings.cfg')
    config.read(config_file)

    textfile = config.get('files','full_text')

    # user must pass a word via command line
    parser = argparse.ArgumentParser(description="A Python tool for calculating word concordance.")
    parser.add_argument('-w', '--word', required=True, help="word you want to see in context")
    args = parser.parse_args()

    word = args.word

    concordword = concordance(textfile, word)
    print(concordword)

if __name__ == '__main__' :
    main()