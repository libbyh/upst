#! /usr/bin/env python
import re
from ConfigParser import SafeConfigParser
import os
import sys

# Create list of lower case words
# define words as `stuff between whitespace(s)'
# \s+ --> match any whitespace(s)
def word_list(textfile):
    textfile = (open(textfile,'r'))
    word_list = re.split('\s+', textfile.read().lower())
    textfile.close()
    return word_list

# Create dictionary of word:frequency pairs
# by default, sorts dictionary by frequency (desc) 
def word_freq(word_list, sort="frequency"):
    freq_dic = {}
    
    # Remove punctuation marks:
    punctuation = re.compile(r'[(.?!,":;\'`)]') 

    # Build the dictionary:
    for word in word_list:
        # remove punctuation marks
        word = punctuation.sub("", word)
        # form dictionary
        try: 
            freq_dic[word] += 1
        except: 
            freq_dic[word] = 1
    
    # sort the dictionary
    if sort == "frequency":
        freq_dic = [(val, key) for key, val in freq_dic.items()]
        # sort by frequency
        freq_dic.sort(reverse=True)
    # if user specificied alphabetical sorting, do that instead
    elif sort == "alphabetical":
        freq_dic = freq_dic.items()
        freq_dic.sort()    
    
    return freq_dic

# print frequency dictionaries
def print_freq(freq_dic):
    for freq, word in freq_dic:
        print word + "," + str(freq)
        
# Main function
if __name__ == '__main__' :
    
    # Get file to use from settings.cfg:
    config = SafeConfigParser()
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, 'settings.cfg')
    config.read(config_file)

    textfile = config.get('files','full_text')
    
    # call the functions that do the counting and sorting
    word_list = word_list(textfile)
    word_count = len(word_list)
    freq_dic = word_freq(word_list)
    unique_word_count = len(freq_dic)
    
    # print the sorted word-frequency pairs
    # use `python words.py > word-freq-pairs.txt' to send output to a text file
    print_freq(freq_dic)