import glob

read_files = glob.glob("religious-texts/quran-in-english-clearquran-verse-by-verse-txt-edition-allah/*.txt")

with open("religious-texts/Quran.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read() + b" ")