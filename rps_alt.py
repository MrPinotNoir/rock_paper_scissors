import random

def game():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)

    user_choice = input("Enter your choice (rock, paper or scissors): ")
    while user_choice not in choices:
        print("Invalid input, try again.")
        user_choice = input("Enter your choice (rock, paper or scissors): ")
    
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "Congratz, you win!"

    else:
        return "U looze :(("



print(game())



