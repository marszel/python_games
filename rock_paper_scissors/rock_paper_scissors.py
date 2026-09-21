import random

choices = ["rock", "paper", "scissors"]

def start_game():
    player = input("Choose rock, paper or scissors: ").lower()
    computer = random.choice(choices)
    if player == computer:
        print(f"It's a tie! Both chose {player}.")
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        print(f"You win! {player} beats {computer}.")
    elif player not in choices:
        print("You have to choose from: rock, paper or scissors.")
    else:
        print(f"Computer wins! {computer} beats {player}.")

continue_playing = True

answer = input("Do you want to play rock paper or scissors? ").lower()
while answer not in ["yes", "no"]:
    answer = input("Choose yes or no. ")
if answer == "no":
    continue_playing = False

while continue_playing:
    start_game()
    answer = input("Do you wanna try again? ")
    while answer not in ["yes", "no"]:
        answer = input("Choose yes or no. ")
    if answer == "no":
        break

print("Maybe next time.")