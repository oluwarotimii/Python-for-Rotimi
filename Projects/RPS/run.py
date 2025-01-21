import random

def game() :
    print('Welcome to the Rock, Paper, Scissors Game!')
    compScore = 0
    humanScore = 0
    while True:
    
        choice = input('Choose on of this options! :')
        options = ['Rock', 'Paper', 'Scissors']
        comp_Choice = random.choice(options)
        # print(comp_Choice)Paper
        # if choice != options:
        #         print('Please enter a valid option,', options)
        if choice == comp_Choice:
            humanScore = humanScore + 1
            print('You win!\nScore is')
        else:
            compScore = compScore + 1
            print('Try again!')
        print('computer:', compScore, ':', humanScore, 'You')

game()