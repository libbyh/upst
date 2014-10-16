#! /usr/env/python

# This script counts lines, sentences, and words of a text file. 
# In order for the output to make sense, it requires each paragraph to be
# one line with no blank lines between paragraphs.

# First, just to be sure, we set all the counters to zero:
lines, paragraphs, sentences, words, chapters, volumes = 0, 0, 0, 0, 0, 0

# Now we need to get a file to work with:
textfile = open('pandp.txt', 'r')

# And now we are going to read one line at a time:
for line in textfile:
    lines += 1
    
    if line.startswith('CHAPTER'):
        chapters += 1
    elif line.startswith('VOLUME') or line.startswith('VOL.'):
        volumes += 1
    elif line.startswith('\n'):
        if prev_line.startswith('\n'):
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
textfile.close()

sentavg = sentences / paragraphs
wordavg = words / paragraphs
paraavg = paragraphs / chapters

# And now print the results:
print '-' * 50
print "COUNTS "
print "Lines      : " + str(lines)
print "Paragraphs : " + str(paragraphs)
print "Chapters   : " + str(chapters)
print "Volumes    : " + str(volumes)
print "Sentences  : " + str(sentences)
print "Words      : " + str(words)
print "\n"
print "AVERAGES"
print "Sentences per paragraph: " + str(sentavg)
print "Words per paragraph: " + str(wordavg)
print "Paragraphs per chapter: " + str(paraavg)