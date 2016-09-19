#! /usr/env/python

# This script counts lines, sentences, and words of a text file. 

from configparser import SafeConfigParser
import os

class TextItem(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

def count_objects(textfile):
    # First, just to be sure, we set all the counters to zero:
    lines, paragraphs, sentences, words, chapters, volumes = 0, 0, 0, 0, 0, 0

    # Now we need to get a file to work with:
    f = open(textfile, 'r')
    
    # And now we are going to read one line at a time:
    for line in f:
        lines += 1
    
        if line.startswith('CHAPTER') or line.startswith('Chapter'):
            chapters += 1
        elif line.startswith('VOLUME') or line.startswith('VOL.'):
            volumes += 1
        elif line.startswith('\n') or line.startswith('\r'):
            if prev_line.startswith('\n') or prev_line.startswith('\r'):
                pass
            else:
                paragraphs += 1
        else:
            # assume that each sentence ends with . or ! or ?
            # so simply count these characters
            sentences += line.count('.') + line.count('!') + line.count('?')
        
            # create a list of words
            # use None to split at any whitespace regardless of length
            # so for instance double space counts as one space
            tempwords = line.split(' ')
        
            # word total count
            words += len(tempwords)
        
        prev_line = line
        
    # We'll be tidy and close the file:
    f.close()

    # create a dictionary of counts to return
    text_items = [TextItem("Lines", lines), TextItem("Paragraphs", paragraphs), 
        TextItem("Chapters", chapters), TextItem("Volumes", volumes), 
        TextItem("Sentences", sentences), TextItem("Words", words), 
        TextItem("Average words/paragraph", words/paragraphs if paragraphs > 0 else "n/a"),
        TextItem("Average sentences/paragraph", sentences/paragraphs if paragraphs > 0 else "n/a"),
        TextItem("Average paragraphs/chapter", paragraphs/chapters if chapters > 0 else "n/a")
        ]
    counts = dict([ (i.name, i.count) for i in text_items ])

    return counts

def main():
    # Get file to use from settings.cfg:
    config = SafeConfigParser()
    script_dir = os.path.dirname(__file__)
    config_file = os.path.join(script_dir, 'settings.cfg')
    config.read(config_file)

    textfile = config.get('files','full_text')
    
    # count the text items - sentences, paragraphs, etc. - in the file
    counts = count_objects(textfile)    
    
    # And now print the results:
    print(counts)

# Call the main function
if __name__ == '__main__' :
    main()