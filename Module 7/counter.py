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
