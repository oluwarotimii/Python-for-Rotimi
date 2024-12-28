# Write a program to read through a file and print it out in upper case
# For this I will use the Practice.md

fileName = input('Enter the File Name: ')
choosenFile = open(fileName)
readFile = choosenFile.read().upper()
print(fileName)
print(len(readFile))
print(readFile)
