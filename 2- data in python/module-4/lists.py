# This is about Lists!!!!!!!!!
listsFile = open('lists.md', 'w')
line1 = ('# Lists \nThis list is a sequence of values, now the values in a list are called ELEMENTS or Items.\n There are many ways to make a list \n-The Simplest way is to use these brackets []')
line2 = ("\nExamples of Lists are : \n-[10, 20, 30, 40]\n-['crunchy dog', 'ram bladder, 'lark vomit'] ")
line3 = ("\nA List also can contain several datatypes like the integer, string, float and also another list")

listsFile.write(line1,)
listsFile.write( line2, )
listsFile.write(  line3)
line4 = ('\n For the list methods we have :\n-Extend,\n-Append,\nThis two are used to add to a list \n-Extend is used to add a list to another list, basically append a list to another list.\n-The Append is used to add an Item to the end of an exsiting list. ')
line5 = ('\nNow for deleting an item on a list the method ```pop()``` is used like years.pop()\nThis removs the last item in the list.\n-Also an argument can be passed in the ()\n-Also we can remove the element if we know it but not the value by using the remove method ```remove(value)```')
listsFile.write(line4)
listsFile.write(line5)
line6 = ('\n-For spliting strings (words) to single alphanet we  use the list functions ( it is in built) ```list()```.\n-To split a sentence into words in to a list we use the ```split()``` also in built')
listsFile.write(line6)

listsFile.close()

file = open('lists.md')
readFile = file.read()

print(readFile)

# Now Main event.
# Example of Lists

names = ['Oluwarotimi', 'Aduramigba', 'Toluwanimi', 'Emmanuel', 'Adewumi', 'Seunayo', 'Oluwasetemi']
years = [2002, 2004, 2005, 2009, 2005, 2055, 1994]

print(names, years)

# So in python the indexing of values in a list starts with 0,1...
# so to access a particular item use the index number like to access the year 2009
print(years[3])

# the index is 3, so to change is to 2008 i use this
years[3] = 2008

print(years[3])

# going to a list the easiest way is to use a loop, a FOR loop
for name in names :
    print(name)

for i in range(len(years))  :
    years[i] = years[i] * 2
    print(years)

years.append(2003)
print(years)

years2 = [2004,2005,2006,2007,2010,2019,2018]
years.extend(years2)

print(years)
name = 'oluwarotimi'
nameList = list(name)
print(nameList) # list is an in built function.
 