import numpy as np
import pygame
import sys
import math

rows_count = 6
columns_count = 7


def create_board():
    return np.zeros((rows_count, columns_count))


def drop_piece(board, row, column, piece):
    board[row][column] = piece


def is_valid_location(board, column):
    return board[rows_count - 1][column] == 0


def get_next_open_row(board, column):
    for row in range(rows_count):
        if board[row][column] == 0:
            return row


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check all horizontal locations
    for column in range(columns_count - 3):
        for row in range(rows_count):
            if board[row][column] == piece and board[row][column + 1] == piece and board[row][column + 2] == piece and \
                    board[row][column + 3] == piece:
                return True

    # Check all vertical locations
    for column in range(columns_count):
        for row in range(rows_count - 3):
            if board[row][column] == piece and board[row + 1][column] == piece \
                    and board[row + 2][column] == piece and board[row + 3][column] == piece:
                return True

    # Check all positively slopped diagonals
    for column in range(columns_count - 3):
        for row in range(rows_count - 3):
            if board[row][column] == piece and board[row + 1][column + 1] == piece \
                    and board[row + 2][column + 2] == piece and board[row + 3][column + 3] == piece:
                return True

    # Check all negatively slopped diagonals
    for column in range(columns_count - 3):
        for row in range(3, rows_count):
            if board[row][column] == piece and board[row - 1][column + 1] == piece \
                    and board[row - 2][column + 2] == piece and board[row - 3][column + 3] == piece:
                return True


def draw_board(board):
    for column in range(columns_count):
        for row in range(rows_count):
            pygame.draw.rect(screen, (0, 0, 0),
                             (column * square_size, row * square_size + square_size, square_size, square_size))
            pygame.draw.circle(screen, (255, 255, 255), (int(column * square_size + square_size / 2),
                                                         int(row * square_size + square_size + square_size / 2)),
                               radius)

        for column in range(columns_count):
            for row in range(rows_count):
                if board[row][column] == 1:
                    pygame.draw.circle(screen, (255, 255, 0),
                                       (int(column * square_size + square_size / 2), square_height -
                                        int(row * square_size + square_size / 2)), radius)
                elif board[row][column] == 2:
                    pygame.draw.circle(screen, (0, 153, 255),
                                       (int(column * square_size + square_size / 2), square_height -
                                        int(row * square_size + square_size / 2)), radius)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False  # As no one has formed the row
turn = 0

pygame.init()

square_size = 100
square_width = columns_count * square_size
square_height = (rows_count + 1) * square_size
total_size = (square_width, square_height)

radius = int(square_size / 2 - 5)

screen = pygame.display.set_mode(total_size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (0,0, square_width, square_size))
            pos_x = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, (255, 255, 0), (pos_x, int(square_size/2)), radius)
            else:
                pygame.draw.circle(screen, (0, 153, 255), (pos_x, int(square_size/2)), radius)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(event.pos) - to get the position of the click
            # Ask for Player 1 Input
            if turn == 0:
                pos_x = event.pos[0]
                column = int(math.floor(pos_x / square_size))
                # column = int(input("Player 1, please make your selection (0-7):"))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 1)

                    if winning_move(board, 1):
                        print("Player 1 has won!!! Congratulations!!!")
                        game_over = True

            # Ask for Player 2 Input
            else:
                pos_x = event.pos[0]
                column = int(math.floor(pos_x / square_size))

                if is_valid_location(board, column):
                    row = get_next_open_row(board, column)
                    drop_piece(board, row, column, 2)

            print_board(board)
            draw_board(board)
            turn += 1
            turn %= 2
