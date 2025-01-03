fileName = open('dict_words.txt', 'w')
line1 = 'But soft what light through yonder window breaks '
line2 = 'It is the east and Juliet is the sun '
line3 = 'Arise fair sun and kill the envious moon '
line4 = 'Who is already sick and pale with grief '

fileName.write(line1)
fileName.write(line2)
fileName.write(line3)
fileName.write(line4)

fileName.close()


#Counting the words, first splittig the text in the files to words and the counting the 
#Counting the words, first splittig the text in the files to words and the counting the words
# We are counting the number of time that a word appears?
fName = input('Please Enter the File Name: ')
try:
    filehand = open(fName)
except:
    print('File can not be opened', fName)
    exit()

counts = dict()
for line in filehand :
    words = line.split()
    for word in words :
        if word not in counts :
            counts[word] = 1
        else:
            counts[word] += 1 
print(counts)
print(words)