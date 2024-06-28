from random import randint

# Create a list of options to play
t = ["Rock", "Paper", "Scissors"]

# Make computer do a random play between 0-2
computer = t[randint(0,2)]

# Set player to False
player = False

while player == False:
# Set player to true
    player = input("Paper, Scissors, Rock? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That is not a valid play, check spelling!")

# Reset player back to False to continue the loop
player = False
computer = t[randint(0,2)]