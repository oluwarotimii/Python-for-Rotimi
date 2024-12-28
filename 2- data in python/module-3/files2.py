
# Letting the user choose the file name

fName = input('Enter the File Name: ')
try:
    filePick = open(fName)
    count = 0
    zcount = 0
    
    for fileLine in filePick :
        if fileLine.startswith('#') :
            count = count + 1
            print('This is line', count)
            print(fileLine)
        else:
            zcount = zcount + 1
            print('Line not found ', zcount)

    
except:
    filePick = -1
    print('File does not Exist!')

print('+++++++++++++++++++++++++++++++===============================++++++++++++++++++++++++++++++')
print('Lines with -', count )
print('Lines without -', zcount )



finder = input("What are you looking for in the file: ")
filePicked = open(fName)


def finder_function() :
    findTimes = 0
    for fileAi in filePicked :
        if  fileAi.find(finder) :
            findTimes = findTimes + 1
        else:
            print( finder, ' not found in file.')

    print('Found ', finder, findTimes, 'times.')

finder_function()
