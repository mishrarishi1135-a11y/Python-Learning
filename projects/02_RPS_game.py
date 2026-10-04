"""
WORKFLOW OF PROJECT:
1- input from user(rock, paper, scissor)
2- computer choice(rock, paper, scissor) and computer will choose randomly not conditionally.
3- result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = paper win
Rock - scissor = Rock win

B- paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Paper = Scissor win
scissor - Rock = Rock win

"""

import random
# first we create a list
item_list = ["Rock","Paper","Scissor"]

# Input from the user
user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)

print(f"user choice = {user_choice}, computer choice = {comp_choice}")

# Now we want to print result who wins.

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer wins")
    else:
        print("Rock smashes Scissor: You wins")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cut the paper: Computer wins")
    else:
        print("Paper covers Rock: You wins")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock break the Scissor: Computer wins")
    else:
        print("Scissor cuts Paper: You wins")