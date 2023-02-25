import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

print("------- ROCK PAPER SCISSORS -------")
while player not in options:
    player = input("Enter a choice: ").lower()

print()
print(f"Player: {player}")
print(f"Computer: {computer}")
print("------------ RESOULT --------------")
if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("You lose!")
print("------------ RESOULT --------------")
