import random

choices = ["rock", "paper", "scissors"]

def start_game():
    computer = random.choice(choices)
    player = input("Choose rock, paper or scissors: ").lower().strip()
    while player not in choices:
        player = input("Invalid choice! Choose rock, paper or scissors: ").lower().strip()
    if player == computer:
        print(f"It's a tie! Both chose {player}.")
    elif (player == "rock" and computer == "scissors") or \
        (player == "paper" and computer == "rock") or \
        (player == "scissors" and computer == "paper"):
        print(f"You win! {player} beats {computer}.")
    else:
        print(f"Computer wins! {computer} beats {player}.")

def get_yes_no_input(prompt):
    current_prompt = prompt
    while True:
        user_choice = input(current_prompt).lower().strip()
        if user_choice in ["yes", "no"]:
            return user_choice
        else:
            current_prompt = "Choose yes or no. "

answer = get_yes_no_input("Do you want to play rock paper or scissors? ")
if answer == "no":
    print("Maybe next time.")
else:
    while True:
        start_game()
        answer = get_yes_no_input("Do you wanna try again? ")
        if answer == "no":
            break

print("Thank you for playing.")