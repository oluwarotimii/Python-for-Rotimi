#this is about files

fhand = open('mob.txt')
print(fhand)

# counting the lines in it 

count = 0
for line in fhand :
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


for readmeLine in readme :
    count = count + 1
    # print('Line 1: ', readmeLines, 'line number', count)
  
    if readmeLine.startswith('##'): 
        print(readmeLine)
  
# print('Line Count: ', count)

