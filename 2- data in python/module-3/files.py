#this is about files

fhand = open('mob.txt')
print(fhand)

# counting the lines in it 

count = 0
for readmeLines in fhand :
    count = count + 1
print('Line Count: ', count)

readme = open('Projects.md')
print(readme)


# for readmeLines in readme :
    # count = count + 1
    # print('Line 1: ', readmeLines, 'line number', count)
    # print('+++++++++++++++++++++++++++++++=======================================+++++++++++++')
    # if readmeLines.startswith('##'): 
        # print(readmeLines)
  
# print('Line Count: ', count)



print('+++++++++++++++++++++++++++++++=======================================+++++++++++++')

#  This is for seearching in a file 
# for readmeLine in readme :
    # count = count + 1
    # print('Line 1: ', readmeLines, 'line number', count)
  
    # if readmeLine.startswith('##'): 
        # print(readmeLine)
  
# print('Line Count: ', count)


# this is for striping the white spaces in lines This is a search Loop

# for readmeLines in readme :
    # readmeLines = readmeLines.rstrip()
    # print(readmeLines)
    # if readmeLines.startswith('###') :
        # print(readmeLines) 




zcount = 0
# skipping uninteresting 
for readmeLines in readme :
    readmeLines = readmeLines.rstrip()
    # Skiping Uninteresting lines
    if not readmeLines.startswith('-') : # this tells us lines that didn't not start with -, here they the uninteresting lines
        count = count + 1
        print("The lines that doesn't start with - are ",count, 'lines')
        continue
    zcount = zcount + 1
    print(readmeLines)

print('++++++++++++++++++++++++-++++++++++++=================================')
print('The number of interesting lines are: ', zcount)
print('The number of unintersting lines are: ', count)

#Using the find String, to find something in  files

newFile = open('Projects.md')

for lines in newFile :
    lines = lines.rstrip()
    if lines.find('AI'):
        count = count + 1
        print(lines)
    else :
        zcount = zcount + 1
        print('AI not found in file')
print('++++++++++++++++++++++++-++++++++++++=================================')

print('AI was found in ', count, ' lines ', "\n Looked through the file and AI wasn't in ", zcount)
