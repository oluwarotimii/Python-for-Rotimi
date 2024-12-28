# This is Chapter 6  about strings
# ? Looking into strings



print('_---------------------------+++++++++++++++++++++++++++++++++===============================__+++++++++++++++++++')
print('INCEPTION')
fruit = 'strawberry'
letter = fruit[3]
fruit_len = len(fruit)   # This is for asking the length of the string
print('numbers of fruit letters', fruit_len)
print('Letter with index 3 is ', letter)



index = 0
#Looping through the strings
while index < fruit_len : # thiss is to say that as long as the index is still les than the number of letters in the word (counting froms zero?)
    fruit_letter = fruit[index] # fruit_letter = to the number of the letter, remeber that this keeps increasing by one? till 10
    print(index, fruit_letter)  # so here as the loop goes through the letters  in the food it prints both the index number and the letter side by side.
    index = index + 1   # this is where it adds and more to the next letter, by add 1 to the index which was zero?
print('END OF PROGRAM')

# using a definite loop


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
# lets count and find a letter in here
count = 0
numbs_a = 0
for fruit_letter in fruit :
    count = count + 1
    # print(fruit_letter)
    if fruit_letter == 'r' :
        numbs_a = numbs_a + 1
        print('R is here!', numbs_a)
        # break
    else :
        print('R is not present', count)
print('Loop number',count)
print('R is here!', numbs_a)

# SLICING STRINGS
# THIS IS HOW WE CAN GO THROUGH THE STRING WITHOUT  LOOPING

full_name = 'Oluwarotimi Adewumi'
#  I WANT TO PRINT ROTIMI IN THE NAME SO NOW WE USE A BOX MODEL TO GET THE INDE NUMBER
print('My name is ', full_name, 'but people like to call me', full_name[5 : 11])
print('Also my surname is ', full_name[12 : 19] )

print('Thanks =======================================')


# CONCATENATION OF STRINGS
#  ALSO TH  IN CAN BE USEDD AS A LOGICAL OPERATOR, IT RETURNS A TRUE OR FALSE.

if 'w' in full_name:
    print('found it !')

print( full_name.upper())
print(full_name.lower())
print(full_name.find('a'))
print(type(full_name))
print(full_name.isdigit())
print(full_name.strip())
print(full_name.capitalize())
print(full_name.startswith('A'))
print(full_name.replace('oluwarotimi', 'Emmanuel'))
print(full_name.lstrip())  # LEFT AND RIGHT STRIP FOR GETTIGN RID OF  WHITESPACES