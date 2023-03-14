import random

def roll_dice():
    min = 1
    max = 6
    roll_again = 'yes'

    while roll_again == 'yes' or roll_again == 'y':
        print('Rolling the dice...')
        print('The number is: ', random.randint(min, max))
        roll_again = input("Roll the dice again? (y/n): ")

print("Welcome to the Dice Rolling Simulator!")
roll_dice()
