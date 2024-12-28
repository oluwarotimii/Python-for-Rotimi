import random


game_score = 0
rand_number = 0
number_guesses = 3

print("Welcome to Frobenius's Guessing Game. \n Please Pick a number")

def start_game() :
    user_number = int(input('What is this number you picked in your mind?'))
    rand_number = random.random(10)