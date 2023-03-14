import random

def guess_number():
    number = random.randint(1, 100)
    count = 0

    while True:
        guess = int(input('Enter your guess between 1 and 100: '))
        count += 1
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number in", count, "tries.")
            break

print("Welcome to the Guess the Number Game!")
guess_number()