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
    size_btwn = w//rows
    x, y = 0, 0
    for l in range(rows):
        x += size_btwn
        y += size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redraw_window(surface):
    global rows, width
    surface.fill((0,0,0))
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global rows, width
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = Snake((0, 0, 255), (10, 10))
    flag = True

    clock = pygame.time.Clock()
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redraw_window(win)
    pass


main()
