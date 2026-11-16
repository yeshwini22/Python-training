import random
choices = ["stone", "paper", "scissors"]
player1 = random.choice(choices)
player2 = random.choice(choices)
print("Player 1:", player1)
print("Player 2:", player2)

if player1 == player2:
    print("It is a tie.")
elif player1 == "stone" and player2 == "scissors":
    print("Player 1 wins.")
elif player1 == "paper" and player2 == "stone":
    print("Player 1 wins.")
elif player1 == "scissors" and player2 == "paper":
    print("Player 1 wins.")
else:
    print("Player 2 wins")