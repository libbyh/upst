# Useful Python Scripts for Texts #


## License and Info ##

This collection of "Useful Python Scripts for Texts" (UPST) was originally constructed for teaching students in an honors academic writing course. Like a lot of open source software, it has two characteristics:

1. it is free to share with others, and
2. it is indebted to more people than I can thank here.

The latter is especially true since I am entirely self-taught when it comes to coding in Python and each of these scripts is the product of a lot of scrutinizing of other scripts and copying of code until I understood how things worked and could write it myself. 

As a way to thank my many teachers, I have tried here to comment the scripts as thoroughly as I could, in the hope that I can help others in the same way I was helped.

All of this work is hereby in the [public domain][].

## Setup ##

1. Copy ```settings_example.cfg``` to ```settings.cfg``` and set ```full_text``` to the right path for your environment.
2. Run ```conda env create -f environment.yml``` to make sure you have all the modules you'll need.

If this is your first time using ```nltk```, you'll probably need to download additional info. See [the NLTK docs](http://www.nltk.org/data.html) for info.

## Usage ##

In order to make these scripts as easy to use as possible, they are designed to be run from the command line. In the case of the latter, output can be captured from `stdout` by simply sending the results to a text file of the user's own naming:

    python pythonscript.py > output.txt

Yup, it's just that easy. 

[public domain]: http://creativecommons.org/publicdomain/

## Recent changes
- updated to use Python 3.5 (anything lower is no longer supported)
- fixed dispersions.py so that it displays graphs for a single word

## Changes from [johnlaudun/upst](https://github.com/johnlaudun/upst) ##

1. I’m working my way through each file editing them to use ```main()``` functions and ```if __name__ == "__main__": main()``` calls. StackOverflow has a few good posts about why to do this. See [What does `if __name__ == “__main__”:` do?](http://stackoverflow.com/questions/419163/what-does-if-name-main-do), for instance. The gist is that declaring and then calling a main function separates the functions from the code that should execute. It also means that stuff in the ```main()``` function happens only when you call it as a standalone script (i.e., not when you use it in other programs).

2. I’m dividing the scripts into sets of functions generally. Why? Functions run faster. Again, [StackOverflow has more info on why](http://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function). Also, functions are cleaner than scripts and can be used in other programs. If you’ve looked at any of my older code on GitHub, you know I used to write straight scripts all the time too. I’ve seen the light.

3. I’m changing the way ```stats.py``` counts lines, paragraphs, words, etc. to accommodate Project Gutenberg texts. In Laudun’s original code, each line was a paragraph, but Project Gutenberg texts have blank lines between paragraphs and multiple lines with paragraphs.

4. I added a ```environment.yml``` file. Each script requires a different set of modules, and it was getting frustrating to have to interrupt my analysis workflow to install them. Now you can install them all at once as soon as you clone the repo. Then you can get to work.
