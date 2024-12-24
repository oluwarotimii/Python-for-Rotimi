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