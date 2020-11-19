import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox


class Cube(object):
    def __init__(self, start, dirnx=0, dirny=0, color=(255, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class Snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def add_cube(self):
        pass

    def draw(self, surface):
        pass


def draw_grid(w, rows, surface):
    pass


def redraw_window(surface):
    pass


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    width, height = 500, 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = Snake((0, 0, 255), (10, 10))
    flag = True

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)
    pass


main()
