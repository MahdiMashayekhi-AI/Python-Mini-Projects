import random

def play_hangman():
    words = ['python', 'programming', 'computer', 'code', 'algorithm', 'world', 'Congratulations']
    word = random.choice(words)
    guessed_letters = set()
    max_attempts = 6
    attempts = 0
    while attempts < max_attempts:
        # Print the hangman figure
        print_hangman(attempts)
        # Print the word with asterisks for unguessed letters
        print(' '.join([letter if letter in guessed_letters else '*' for letter in word]))
        # Ask the user for a guess
        guess = input('Enter a letter: ')
        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print('Congratulations! You guessed the word!')
                return
        else:
            attempts += 1
            print('Incorrect. You have', max_attempts - attempts, 'attempts left.')
    print('Sorry, you ran out of attempts. The word was', word)

def print_hangman(attempts):
    if attempts == 0:
        print('_________')
        print('|       |')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('=========')
    elif attempts == 1:
        print('_________')
        print('|       |')
        print('|       O')
        print('|       ')
        print('|       ')
        print('|       ')
        print('|       ')
        print('=========')
    elif attempts == 2:
        print('_________')
        print('|       |')
        print('|       O')
        print('|       |')
        print('|       |')
        print('|       ')
        print('|       ')
        print('=========')
    elif attempts == 3:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|')
        print('|       |')
        print('|       ')
        print('|       ')
        print('=========')
    elif attempts == 4:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|       |')
        print('|       ')
        print('|       ')
        print('=========')
    elif attempts == 5:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|       |')
        print('|      /')
        print('|       ')
        print('=========')
    else:
        print('_________')
        print('|       |')
        print('|       O')
        print('|      /|\\')
        print('|       |')
        print('|      / \\')
        print('|       ')
        print('=========')

# Start the game
play_hangman()
