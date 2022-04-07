

import pygame
from constants import *
from board import *
from characters import *
from game import *


clickX, clickY = 0, 0

def main():
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(100)
    start = True
    SCREEN 
    board = Board()
    board.draw_board()
    create_spaces()
    create_all_characters()
  
    while start:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                start = False
   
        run()
        pygame.display.update()


main()