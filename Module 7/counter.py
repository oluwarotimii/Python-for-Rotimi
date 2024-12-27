# to count how many times we exeute a loop,

shaxan = 0
biggest = 0

for thing in [12,3,4,5, 45, 6, 45, 45, 34, 545, 45, 45, 67, 343, 334,] :
    shaxan = shaxan + 1
    print(shaxan, thing)
    if thing > biggest :
        print('This is the current number ', thing)
        biggest = thing
        print('This is the new Biggest ', biggest)
print('This is the ', shaxan, 'time we are running this loop !')


#this is an exmaple of a counting loop, I added my own modifications of previous examples into one


# the Summing Loop

zork = 0
# zork is the counter fot the loop
print ('The inception of this program', zork)
for  samples in [23,434,34,5,45,6,5,67,78,7,89,8,9,56,56,56,56,3,7,834,767,45,56,23,65,23,756,23,56,23,56,234,6,23,56,76,23,56] :
    #  we are going to be adding the loop number to the numbers
    zork = zork + 1
    print( 'Loop number is ', zork)
    print('+++++++++++++++++++++++++++++')
    zamps = zork + samples
    print(zork, samples)
    print('loop + samples', zamps)
    # print(zork, samples)
print('=====================================================================')
print('final loop number', zork)


#sum again

count = 0
sum = 0
print('Inception', count, sum)
for value in [23,23,23,23,233,23,4345,232,4,45456,7676,878,4,5,34,6778,3432323,766,8987767,34,623,98928,94,25,6869,7898,96055,3993480,48574,38498] :
    count = count + 1 #loop number
    sum = sum + value # give sum another number which adding sum and value
    print('count, sum, value', count, sum, value)
print('The end', count, sum, '\nAverage: ', sum/count)


# Foltering in a loop

print('Inception')
for numbs in [1,2,3,45,56,77,88,89,45,67,34,8,97,856] :
    if numbs > 90 :
        print('THE Largest Number is: ', numbs)
print('The End, Largest number is :',  numbs)


# finding a number using boolean varibale to indicate
print('INCEPTION')
found = False
loop = 0
print('++++++++++++++++++++++')
print('Found? ',found)

for value in [12,34,45,67,5,3,34,67,45,8,596,562,1,56,0,67,56] :
    loop = loop + 1
    print('The Value is: ', value, ' And the loop number is:  ', loop)
    if value == 0 :
        found = True
        print('The value was found.')
        break
    else:
        print('NOT FOUND!')
print('END OF PROGRAM!')

#for the smallest value

# we are going to be using none type
print('INCEPTION')
smallest = None  # here  means the numbers we have seen as the smallest is nothing
#  also the use of is  because is  way more powerful tan equals too

print('+++++++++++++++++++++++++++++++++==============================++++++++++++++++++++++++++')

for value in [3,23,4,34,56,2,3,2,56,76,34,5,634,56,34,67,34,56,23,78,98] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print('Smallest', smallest, 'Value', value)
print('END OF PROGRAM', smallest)