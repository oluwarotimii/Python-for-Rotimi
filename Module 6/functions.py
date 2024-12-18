# here it is all about functions

# the patterns for code are
#Sequential
# Conditional
# iterations
# Store and reuse

# this is store and reuse def is the keyword to define a function 
# built in funtions are float, int , str and others
# the def function just remebers the code you must always invoke the function to use it 

x = 5
print('Hello', x)

def print_lyrics():
    print("I'm on top of the world, in front of the crowd!")
    print('When I get older, I will be stronger...')

print('songs, songs, songs')
x = x + 155
print(x)
print('Thank you')
print_lyrics() # invoking the funcntions


# functions for different greetings in different languages

def greet(lang):
    if lang == 'en':
        print('Hello')
    elif lang == 'fr':
        print('bonjour')
    elif lang == 'es':
        print('Holla')
    else:
        print('Hello, Holla, Bonjour?')
     
# greet('ee')

# LEts do this with the return statement

