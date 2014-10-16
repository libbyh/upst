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
def word_freq(word_list):
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
    
    return freq_dic

# If you want to sort words by frequency (descending), use this:
def freq_sorted_dic(freq_dic):
    # create list of (val, key) tuple pairs
    freq_dic_sorted = [(val, key) for key, val in freq_dic.items()]
    # sort by frequency
    freq_dic_sorted.sort(reverse=True)
    return freq_dic_sorted
    
# If you want to sort words by alphabetical order, use this:
def alpha_sorted_dic(freq_dic):
    freq_dic_sorted = freq_dic.items()
    freq_dic_sorted.sort()
    return freq_dic_sorted

# print frequency dictionaries
def print_freq(freq_dic):
    for freq, word in freq_dic:
        print word + "," + str(freq)
        
# Main function
def main():
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
    freq_dic_sorted = freq_sorted_dic(freq_dic)
    
    # print the sorted word-frequency pairs
    # use `python words.py > word-freq-pairs.txt' to send output to a text file
<<<<<<< HEAD
    print_freq(freq_dic_sorted)
=======
    print_freq(freq_dic)

if __name__ == '__main__' :
    main()
    
>>>>>>> 92c5baf854021e3c786745b5b08529a2f47087ce
