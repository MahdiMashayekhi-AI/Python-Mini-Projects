import random

def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    while True:
        user_choice = input('Choose rock, paper, or scissors: ').lower()

        if user_choice not in options:
            print('Invalid choice. Please try again.')
            continue

        print('You chose', user_choice)
        print('The computer chose', computer_choice)

        if user_choice == computer_choice:
            print('Its a tie!')
        elif user_choice == 'rock' and computer_choice == 'scissors':
            print('-----Rock beats scissors. You win!')
        elif user_choice == 'paper' and computer_choice == 'rock':
            print('-----Paper beats rock. You win!')
        elif user_choice == 'scissors' and computer_choice == 'paper':
            print('-----Scissors beat paper. You win!')
        else:
            print('-----Sorry, you lose!')

        play_again = input('Play again? (y/n): ').lower()
        if play_again == 'n' or play_again == 'no':
            break

print('Welcome to the Rock Paper Scissors Game!')
play_game()