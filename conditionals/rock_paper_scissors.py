import random
import math

print("Welcome to Rock, Paper, Scissors game")

rounds = int(input("\nHow many rounds would you like to play: "))
player_score = 0
comp_score = 0
options = ["Rock", "Paper", "Scissors"]

for round_num in range(rounds):
    print("\nRound", round_num+1)

    player_pick = input("Time to pick... Rock, Paper, or Scissors: ").title()
    comp_pick = random.choice(options)

    if player_pick == comp_pick:
        print("\t\t\tComputer:", comp_pick)
        print("\t\t\tPlayer:", player_pick)
        print("\t\t\tPlayer:", player_score, "\t\t\tComputer:", comp_score)
        print("\t\t\tIt's a tie!")
    elif player_pick == "Rock" and comp_pick == "Scissors" or player_pick == "Scissors" and comp_pick == "Paper" or player_pick == "Paper" and comp_pick == "Rock":
        player_score += 1
        print("\t\t\tComputer:", comp_pick)
        print("\t\t\tPlayer:", player_pick)
        print("\t\t\tPlayer:", player_score, "\t\t\tComputer:", comp_score)
        print("\t\t\tPlayer wins round", round_num+1)
    elif comp_pick == "Rock" and player_pick == "Scissors" or comp_pick == "Scissors" and player_pick == "Paper" or comp_pick == "Paper" and player_pick == "Rock":
        comp_score += 1
        print("\t\t\tComputer:", comp_pick)
        print("\t\t\tPlayer:", player_pick)
        print("\t\t\tPlayer:", player_score, "\t\t\tComputer:", comp_score)
        print("\t\t\tComputer wins round", round_num+1)
    elif player_pick != options:
        print("\t\t\tTry again!")
    else:
        break

if player_score > comp_score:
    print("\nFinal score")
    print("Player:", player_score, "\t\t\tComputer:", comp_score)
    print("You win the game!")
elif player_score == comp_score:
    print("\nFinal score")
    print("Player:", player_score, "\t\t\tComputer:", comp_score)
    print("You tied the game!")
else:
    print("\nFinal score")
    print("Player:", player_score, "\t\t\tComputer:", comp_score)
    print("You lose the game!")

