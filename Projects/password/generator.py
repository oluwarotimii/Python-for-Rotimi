# Password generator
import random
import string


p = dict()
def password_generator()  :
    passwordLetters = string.ascii_letters
    passwordLetters = list(passwordLetters)
    smallLetters = passwordLetters[0:25]
    capitalLetters = passwordLetters[26:]
    passwordNumbers = '0123456789'
    passwordNumbers = list(passwordNumbers)
    passwordSymbols = "!@#$%^&*()_-="''".><,`!\?/;:"
    passwordSymbols = list(passwordSymbols)


    newUletters = random.choices(capitalLetters, k=3)
    newSletters = random.choices(smallLetters, k=3)
    newSymbol = random.choices(passwordSymbols, k=3git)
    newNumbers = random.choices(passwordNumbers, k=3)

    password = newUletters + newSletters + newSymbol + newNumbers
    

    
    
    print(passwordLetters)
    print('\n', smallLetters)
    print('\n', capitalLetters)
    print('\n', passwordNumbers)
    print('\n', passwordSymbols)
    print('\n', newUletters)
    print('\n', newSletters)
    print('\n', newNumbers)
    print('\n', newSymbol)

    print(password)


password_generator()