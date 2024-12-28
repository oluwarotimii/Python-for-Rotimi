import random


game_score = 0
rand_number = 0
# number_guesses = 3

print("Welcome to Frobenius's Guessing Game. \n Please Pick a number")

def start_game() :
    number_guesses = 3
    user_number = int(input('What is this number you picked in your mind?  '))
    
    number_guesses = number_guesses - 1
    rand_number = random.randint(0,10)
    # print(rand_number)
    

    if rand_number == user_number :
        print('You Guessed right!, the number i Picked was ', rand_number)
        game_score = game_score + 1
    else:
        while number_guesses > 0:
            print('You have ', number_guesses, ' trial left. Try again.')
            user_number = int(input('Try again! What number did you pick in your mind?  '))
            number_guesses = number_guesses - 1
            if user_number == rand_number:
                print('You Win!, after ', number_guesses, ' guesses hahaha')
            else:
                print(' Game Over ', number_guesses, 'guesses.')
            


start_game()

