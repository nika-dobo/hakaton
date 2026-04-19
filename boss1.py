# Boss: Rock Paper Scissors!
# Rules of the "Rock, Paper, Scissors" game are:

# Rock beats Scissors
# Scissors beat Paper,
# Paper beats Rock.
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples:
# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

# Test Cases:
#        Rock_Paper_Scissors(('rock', 'scissors'), "Player 1 won!")
#        Rock_Paper_Scissors('scissors', 'rock'), "Player 2 won!")
#        Rock_Paper_Scissors('scissors', 'paper'), "Player1 won!")

def Rock_Paper_Scissors(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif player1 == "rock" and player2 == "scissors":
        return "Player 1 won!"
    elif player1 == "scissors" and player2 == "paper":
        return "Player 1 won!"
    elif player1 == "paper" and player2 == "rock":
        return "Player 1 won!"
    else:
        return "Player 2 won!"

print(Rock_Paper_Scissors("rock", "scissors"))
print(Rock_Paper_Scissors("scissors", "rock"))
print(Rock_Paper_Scissors("scissors", "paper"))