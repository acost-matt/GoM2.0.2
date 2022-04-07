import pygame
from constants import *

all_spaces = []

class Board():
    def __init__(self):
        self.rect = pygame.Rect(BOARDSTART[0], BOARDSTART[1], SQUARE_SIZE * ROWS, SQUARE_SIZE * COLS)
        self.board = pygame.draw.rect(SCREEN, GREY, self.rect)


    def draw_board(self):
        for space in all_spaces:
            if (space.col - space.row) % 2 == 0:
                pygame.draw.rect(SCREEN, space.color, ((space.col * SQUARE_SIZE) + BOARDSTART[0], (space.row * SQUARE_SIZE) + BOARDSTART[1], SQUARE_SIZE, SQUARE_SIZE))
            elif (space.col - space.row) % 2 == 1:
                pygame.draw.rect(SCREEN, space.color, ((space.col * SQUARE_SIZE) + BOARDSTART[0], (space.row * SQUARE_SIZE) + BOARDSTART[1], SQUARE_SIZE, SQUARE_SIZE))

                

    
class Space(Board):
    def __init__(self, col, row):
        super().__init__()
        self.col = col
        self.row = row
        self.rect = pygame.Rect(BOARDSTART[0] + (SQUARE_SIZE * col), BOARDSTART[1] + (SQUARE_SIZE * row), SQUARE_SIZE, SQUARE_SIZE)
        self.filled = False
        self.color = None
        self.team = None
    
    def __repr__(self):
        rep = '(' + str(self.col) + ', ' + str(self.row) + ')'
        return rep

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)


def create_spaces():
    all_spaces.clear()
    for col in range(COLS):
        for row in range(ROWS):
            print(col)
            space = Space(col, row)
            all_spaces.append(space)
            if (space.col - space.row) % 2 == 0:
                space.color = GREY
            elif (space.col - space.row) % 2 == 1:
                space.color = WHITE

def reset_color():
    for space in all_spaces:
        if (space.col - space.row) % 2 == 0:
            space.color = GREY
        elif (space.col - space.row) % 2 == 1:
            space.color = WHITE


        