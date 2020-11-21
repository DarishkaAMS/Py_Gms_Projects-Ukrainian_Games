import numpy as np

rows_count = 7
columns_count = 7


def create_board():
    return np.zeros((rows_count, columns_count))


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valid_location(board, column):
    return board[rows_count-1][column] == 0


def get_next_open_row(board, column):
    for row in range(rows_count):
        if board[row][column] == 0:
            return row


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check all horizontal locations
    for column in range(columns_count-3):
        for row in range(rows_count):
            if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
                return True

    # Check all vertical locations


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

            if winning_move(board, 1):
                print("Player 1 has won!!! Congratulations!!!")
                game_over = True

    # Ask for Player 2 Input
    else:
        column = int(input("Player 2, please make your selection (0-7):"))

        if is_valid_location(board, column):
            row = get_next_open_row(board, column)
            drop_piece(board, row, column, 2)

    print_board(board)
    turn += 1
    turn %= 2

