# this is where the inttleigence of the computer starts to come in 

 # here we are checkinh for the smaller and  bigger nummber. 
# Conditional, indents is needed by 4 spaces
x = 5
if x < 10:
    print("X is Smaller") #Conditional code
if x > 20:
    print('Bigger')
print('The End')  #Sequential code

 # Comparison Operators
 # == Equal to
# <= Greater than or equal to
# >= Less than or equal
# != Not Equal to

# Start seeing code like blocks because of nested code

x = float(input('Enter  a Number: '))
if x > 10: 
    print ('Number is Greater than 10')
if x <= 10:
    print ('Number is Less than or equal to 10')
    if x == 10:
        print('Number is Equal to 10')
        print(x, 'is the number') # two indents
print('Finished')

# so we have Else two way decision

y = float(input('Enter number Y: '))

if y > 100:
    print( 'Y is greater than 100')
    if y == 100:
        print('Y is equal to 100')
else:
    print('Y is less than 100')
print('Finished')

# Try and Except : A way to catch a traceback like an error
# this is used when you have a code that can blow back

name = 'Rotimi'
try:
    newName = int(name)
except:
    newName = -1, ('failed')
print('first : ', newName)

age = '23'
try:
    newAge = int(age)
except:
    newAge = -1, ('failed')
print('Age : ', newAge)

 # this is like an insurance policy for your code
