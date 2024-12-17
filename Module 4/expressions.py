# Expressions
x = 12
y = 2
z = x+y
print(z)
 # the answer is  14 here is added commas  by mistake it turned  it to a tuple thereby throwinf the error.
 # Practising naming  for variables  by calculating Speed and Velcit

distanceTravalled = 100 #meters
timeTaken = 10 # seconds

speed = distanceTravalled / timeTaken

print(speed)
  

  # this is another acceptable naming format
  # the point is that it as  to  be Mnemonic (reasonable to humans)
distance = 100 #meters
time = 10 # seconds

speed = distanceTravalled / timeTaken

print(speed)

# Here python converts the result SPEED to float as againt the python 2 format this was talked abou in the course.

# Next is the Operator Precedence
#here we cite examples that show the precedence of operators
x =  1 + 39 ** 3 % 2 * 2
print (x)
 # this is an exammple with out  the parenthenses.
#  this is what it will look like with parenthenses
newX = 1 +(((39 ** 3) % 2 ) * 2)
print(newX)

# if this correct it showuld give the same answer? GOOD


# TYPES the types here is just used to tell the data type of a variable here is how it is used.
#  Going bak to previous  examples..

type(newX)
type(speed)

print( type(newX))   # this should give an Integer

# lets try this

firstName = 'Oluwarotimi'

print(type(firstName)) # this  should give a string

#Converting datatypes?

# x = '123'
# x = x +1,


# user Input : here we are going to be testing user input with the  Speed calculations

print('Welcome continue to calculate Speed')
userDistanceTravalled = (float(input('Enter the  Distance Travelled (in meters): ')))
userTimeTaken = (float(input('Enter Time Taken (in seconds): ')))

userSpeed = userDistanceTravalled / userTimeTaken
print(str(userSpeed) + ' m/s') 

# Thanks.

# PART 3