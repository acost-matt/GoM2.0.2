import pygame
from characters import Character
from constants import *

class Crown():
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect
        self.character = Character(None, CROWNRECT, None, None)
        self.selected = False

    def get_rect(self):
        self.rect = self.character.rect
    
    def select(self):
        self.selected = True
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def drag(self, x, y):
        self.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = x, y
    
    def reset(self):
        self.rect = CROWNRECT
        self.selected = False

crown = Crown(CROWNIMAGE, CROWNRECT)