# ask user to make choice
# if choice is not valid
#   print an KeyError
# let the computer make a choice
# print the choices selected by both the computer and User
# determine the winner
# ask the user if they want to continue
# if not
#   terminate the program
import random
emojis = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock,Paper or Scissors ? (r/p/s)").lower()
    if user_choice not in choices:
        print("Invalid choice!!")
        continue

    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'The computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')
    elif user_choice == 'r' and computer_choice == 's' or user_choice == 's' and computer_choice == 'p':
        print('You win')
    else:
        print('You lose')

    continueprompt = input('Do you wish to continue? (y/n): ').lower()
    if continueprompt == 'n':
        break
