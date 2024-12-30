# Here we deal wwith text parsing, just like the text form the dict_words.txt but this time they have puntuation.

import string


fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print('File could not be opened. ', fname)
    exit()

counts = dict()

for line in fhand :
    line = line.rstrip()

    line = line.translate(line.maketrans(" ", " ", string.punctuation))
    line =  line.lower()
    words = line.split()

    for word in words :
        if word not in counts:
            counts[word] =  1
        else:
            counts[word] += 1
print(counts)      