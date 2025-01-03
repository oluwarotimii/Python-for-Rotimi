#building tuples
import string

names = 'rotimi', 'iyanu', 'adewumi'
names1 = 'rotimi1', 'iyanu1', 'adewumi1'

print(names, '\n', names1)
print(type(names))

na = tuple('rotimi',)

print(na)

# fileName = open('romeo.txt')
# fhand = fileName.read()
# fhand = fhand.strip()
# fhand = fhand.translate(fhand.maketrans(" ", " ", string.punctuation))
# fhand = fhand.upper()
# print(fhand)

# words = tuple(fhand)
# print(words)