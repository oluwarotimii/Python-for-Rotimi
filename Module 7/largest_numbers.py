# here we are going to be workinng here writing the code  to find the largest number

#  we are going to do this with  loops

print('Printing the largest number')
print('+++++++++++++++++')
 
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [92, 82, 58, 93 ,3,2,8,3,393,9348,98,54] :
    if the_num  > largest_so_far:
        largest_so_far = the_num
        print('largest_so_far', the_num)
print('The Actual Largest Number is ', largest_so_far)