import random

s = ['Rock', 'Paper', 'Scissors']

computer = s[random.randint(0, 2)]  # Computer's choice

value = False

while not value:

    player = input("Rock, Paper, Scissors?")

    if player in s:
        if player == computer:
            print("It's a tie.. Please try again..", player, "equals", computer)
        elif player == "Rock" and computer == "Paper":
            print("Computer wins..!", computer, "covers", player)
        elif player == "Rock" and computer == "Scissors":
            print("Player wins..!", player, "covers", computer)
        elif player == "Paper" and computer == "Rock":
            print("Player wins..!", player, "covers", computer)
        elif player == "Paper" and computer == "Scissors":
            print("Computer wins..!", computer, "covers", player)
        elif player == "Scissors" and computer == "Rock":
            print("Computer wins..!", computer, "covers", player)
        elif player == "Scissors" and computer == "Paper":
            print("Player wins..!", player, "covers", computer)
    else:
        print("Please enter a valid value and re execute the program again.")
        break

    value = False
    computer = s[random.randint(0, 2)]
