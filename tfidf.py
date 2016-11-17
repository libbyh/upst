# from https://gist.github.com/sloria/6407257

import math
from textblob import TextBlob as tb
from collections import Counter

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

document1 = tb(open("religious-texts/King James Bible.txt").read())

document2 = tb(open("religious-texts/Quran.txt").read())

# document1 = tb("""Python is a 2000 made-for-TV horror movie directed by Richard
# Clabaugh. The film features several cult favorite actors, including William
# Zabka of The Karate Kid fame, Wil Wheaton, Casper Van Dien, Jenny McCarthy,
# Keith Coogan, Robert Englund (best known for his role as Freddy Krueger in the
# A Nightmare on Elm Street series of films), Dana Barron, David Bowe, and Sean
# Whalen. The film concerns a genetically engineered snake, a python, that
# escapes and unleashes itself on a small town. It includes the classic final
# girl scenario evident in films like Friday the 13th. It was filmed in Los Angeles,
#  California and Malibu, California. Python was followed by two sequels: Python
#  II (2002) and Boa vs. Python (2004), both also made-for-TV films.""")

# document2 = tb("""Python, from the Greek word (πύθων/πύθωνας), is a genus of
# nonvenomous pythons[2] found in Africa and Asia. Currently, 7 species are
# recognised.[2] A member of this genus, P. reticulatus, is among the longest
# snakes known.""")

bloblist = [document1, document2]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))