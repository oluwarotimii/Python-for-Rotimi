# here i will do a practice task to learn about conditional statements

#what if i write a program to ask for the age of a person and then tell them if they are eligible to vote or not. 
name = str(input('What is your name: '))
age = int(input('Enter you age: '))

# year_left = /18 - age 

# def years_to_vote  (age):
#      try:
#         year_left = 18 - age
#         print(year_left)
#      except:
#         print('invalid')
#     # years_to_vote()

try:
    name = str(name)
    print('name')
except:
    print('invalid input')
print('name accepted')

try:
    age - int(age)
    print (age)
except:
    print('invalid Input')

print ('Age Accepted')

print('Details Accepted', name, 'is', age, ' years old.')


#  lets try  to write a function to calculate how many years to be eligible to vite

        

if age >= 18:
    print('You are Eligible to Vote !')
else:
    
    print('Ooops, not Eligible yet, try again in ', year_left, 'years')  