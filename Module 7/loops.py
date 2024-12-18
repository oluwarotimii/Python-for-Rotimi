#  The iteration variable  keeps it becomoing an infite loop

#  to break out of a loop we use the break keyword
#  to continue to the next iteration we use the continue keyword this skips to the top of the loop


age = int(input('Enter you age: '))
while age == 21:
    print('your current age is ', age)
    age +=1   # continue to increase the age

print('You are  eligbile to drink Alcohol you have turned 21 years old', )
# The While loop is an indefinite  loop

#  the for loop, this is a definte loop

for i in [5, 4, 3, 2, 1, 0] :
    print(i)
print('Loop done!')