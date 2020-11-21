import numpy as np


def create_board():
    return np.zeros((7, 7))


board = create_board()
game_over = False # As no one has formed the row
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        selection = int(input("Player 1, please make your selection (0-6):"))
    # Ask for Player 2 Input
    else:
        selection = int(input("Player 2, please make your selection (0-6)"))

    turn += 15
    turn %= 2

