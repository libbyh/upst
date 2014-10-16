# Useful Python Scripts for Texts #


## License and Info ##

This collection of "Useful Python Scripts for Texts" (UPST) was originally constructed for teaching students in an honors academic writing course. Like a lot of open source software, it has two characteristics:

1. it is free to share with others, and
2. it is indebted to more people than I can thank here.

The latter is especially true since I am entirely self-taught when it comes to coding in Python and each of these scripts is the product of a lot of scrutinizing of other scripts and copying of code until I understood how things worked and could write it myself. 

As a way to thank my many teachers, I have tried here to comment the scripts as thoroughly as I could, in the hope that I can help others in the same way I was helped.

All of this work is hereby in the [public domain][].

## Setup ##

- Copy ```settings_example.cfg``` to ```settings.cfg``` and set ```full_text``` to the right path for your environment.
- Run ```pip install -r requirements.txt``` to make sure you have all the modules you'll need.

If this is your first time using ```nltk```, you'll probably need to download additional info. See [the NLTK docs](http://www.nltk.org/data.html) for info.

## Usage ##

In order to make these scripts as easy to use as possible, they are designed to be run from the command line. In the case of the latter, output can be captured from `stdout` by simply sending the results to a text file of the user's own naming:

    python pythonscript.py > output.txt

Yup, it's just that easy. 

[public domain]: http://creativecommons.org/publicdomain/
