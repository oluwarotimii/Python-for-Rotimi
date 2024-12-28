# Wroting in files

# TO write in files you have to open with  w like this
fout = open('practice.md', 'w')
print(fout)

# The Practice file wasn't present before so it was created be careful if it existed before it will delete the old data
line1 = "# This is s file I created with a python program \n So I wanted to do this to learn how to manipulate and use files in python."
fout.write(line1)
line2 = '\n-Something I have learnt so far is the used of the ``write()`` method, \n also the use os the (w) to signify that the file was opened in the write mode.'
fout.write(line2)

line3 = ' \n-Now the next thing is to use the ```close()``` method to close the file \n and make sure the last bit of data is physically written in the file.'

fout.write(line3)

line4 = ('\n-The use of the ```repr()`` method so it helps to make sure everything returns as a string.\n-Now there is also the use of ((forward slash and t for tab?)1\t 2, 1\t 3 and 1\n3 (forward slash and n for new line?))')
fout.write(line4)
fout.close()