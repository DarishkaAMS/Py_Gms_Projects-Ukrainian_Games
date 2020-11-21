import numpy as np

rows_count = 7
columns_count = 7


def create_board():
    return np.zeros((7, 7))


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valid_location(board, column):
    return board[6][column] == 0


def get_next_open_row(board, column):
    for row in range(rows_count):
        if board[row][column] == 0:
            return row


def print_board(board):
    print(np.flip(board,0))


board = create_board()
print_board(board)
game_over = False # As no one has formed the row
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        column = int(input("Player 1, please make your selection (0-7):"))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 1)

    # Ask for Player 2 Input
    else:
        column = int(input("Player 2, please make your selection (0-7):"))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

    print_board(board)
    turn += 1
    turn %= 2

