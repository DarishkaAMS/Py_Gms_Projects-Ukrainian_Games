import numpy as np


def create_board():
    return np.zeros((7, 7))


def drop_piece():
    pass


def is_valid_location(board, column):
    return board[6][column] == 0


def get_next_open_row():
    pass

board = create_board()
game_over = False # As no one has formed the row
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1, please make your selection (0-7):"))
    # Ask for Player 2 Input
    else:
        column = int(input("Player 2, please make your selection (0-7)"))

    turn += 1
    turn %= 2

