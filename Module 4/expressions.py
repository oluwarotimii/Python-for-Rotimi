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
# Expressions
x = 12
y = 2
z = x + y
print(f"The sum of {x} and {y} is {z}")

# Practising naming for variables by calculating Speed and Velocity
distance_traveled = 100  # meters
time_taken = 10  # seconds

speed = distance_traveled / time_taken
print(f"The speed is {speed} m/s")

# Another acceptable naming format
distance = 100  # meters
time = 10  # seconds

speed = distance / time
print(f"The speed is {speed} m/s")

# Next is the Operator Precedence
x = 1 + 39 ** 3 % 2 * 2
print(f"The result of the expression is {x}")

# Example with parentheses
new_x = 1 + (((39 ** 3) % 2) * 2)
print(f"The result of the expression with parentheses is {new_x}")

# TYPES
print(type(new_x))  # This should give an Integer
print(type(speed))  # This should give a Float

# Let's try this
first_name = 'Oluwarotimi'
print(type(first_name))  # This should give a String

# Converting data types
x = '123'
x = int(x) + 1
print(x)

# User Input: Testing user input with Speed calculations
print('Welcome to the Speed Calculator!')
user_distance_traveled = float(input('Enter the Distance Traveled (in meters): '))
user_time_taken = float(input('Enter Time Taken (in seconds): '))

user_speed = user_distance_traveled / user_time_taken
print(f"The speed is {user_speed} m/s")

# Part 3 for Expressions
