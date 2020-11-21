import numpy as np


def create_board():
    return np.zeros((7, 7))


board = create_board()

# As no one has formed the row
game_over = False
