import random
import string

print("Welcome to Oluwarotimi's password generator! ")
length = int(input('Please Enter length of password you want: '))

def passwordGenerator() :
    numbers = string.digits
    symbols = string.punctuation
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    allCharacters = numbers + symbols + lowercase + uppercase

    # print(allCharacters)
    password = random.choices(allCharacters, k=length)
    password = ''.join(password)

    print("Your password is : ",password)

passwordGenerator()