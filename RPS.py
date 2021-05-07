import random

# Set variables and print both moves out
moves = ["rock", "paper", "scissors"]
player_move = input("Rock, Paper or Scissors...\n")
computer_move = moves[random.randint(0, len(moves) - 1)]
print("Player move: ", player_move.title())
print("Computer move: ", computer_move.title())


# Method for testing win conditions
def game(p_move, c_move):
    if computer_move == player_move.lower():
        print("Tie! Both players used {}!".format(c_move.title()))
    elif computer_move == moves[0] and player_move.lower() == "paper":
        print("Player wins! {} beats {}!".format(p_move.title(), c_move.title()))
    elif computer_move == moves[0] and player_move.lower() == "scissors":
        print("Computer wins! {} beats {}!".format(c_move.title(), p_move.title()))
    elif computer_move == moves[1] and player_move.lower() == "rock":
        print("Computer wins! {} beats {}!".format(c_move.title(), p_move.title()))
    elif computer_move == moves[1] and player_move.lower() == "scissors":
        print("Player wins! {} beats {}!".format(p_move.title(), c_move.title()))
    elif computer_move == moves[2] and player_move.lower() == "rock":
        print("Player wins! {} beats {}!".format(p_move.title(), c_move.title()))
    elif computer_move == moves[2] and player_move.lower() == "paper":
        print("Computer wins! {} beats {}!".format(c_move.title(), p_move.title()))
    else:
        print("You broke it! Input a proper move!")


# Calling the method used to determine a winner
game(player_move, computer_move)
