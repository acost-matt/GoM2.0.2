from calendar import c
import pygame, time
import random

from constants import BLUE, RED, SCREEN

# Load images
dice1_image = pygame.image.load("assets/dice1.png").convert_alpha()
dice2_image = pygame.image.load("assets/dice2.png").convert_alpha()
dice3_image = pygame.image.load("assets/dice3.png").convert_alpha()
dice4_image = pygame.image.load("assets/dice4.png").convert_alpha()
dice5_image = pygame.image.load("assets/dice5.png").convert_alpha()
dice6_image = pygame.image.load("assets/dice6.png").convert_alpha()

false_dice_rect = pygame.Rect(240, 240, 240, 240)
true_dice_rect = pygame.Rect(1440, 240, 240, 240)
all_dice_images = [dice1_image, dice2_image, dice3_image, dice4_image, dice5_image, dice6_image]

class Dice():
    def __init__(self, rect, team):
        self.rect = rect
        self.team = team
        self.value = None
        self.image = None

    def draw(self):
        if self.team:
            pygame.draw.rect(SCREEN, BLUE, self.rect)
            SCREEN.blit(self.image, self.rect)
        else:
            pygame.draw.rect(SCREEN, RED, self.rect)
            SCREEN.blit(self.image, self.rect)

# Indexed list to reference all the faces
all_dice = [Dice(false_dice_rect, False), Dice(true_dice_rect, True)]

               
### Function to perform the random parts of the game               
def roll_dice():
    start_time = time.time()
    true_roll   = random.randint(0, 5)
    false_roll = random.randint(0, 5)
    team = None
    if true_roll > false_roll:
        team = True
    elif false_roll > true_roll:
        team = False
    elif false_roll == true_roll:
        team = None
    for dice in all_dice:
        if dice.team == False:
            dice.value = false_roll
        else:
            dice.value = true_roll

    return [team, false_roll, true_roll]

def attack_dice(team):
    target_roll   = random.randint(0, 5)
    character_roll = random.randint(0, 5)
    team = None
    if character_roll > target_roll:
        return True
    elif target_roll > character_roll:
        return False
    else:
        return None
    for dice in all_dice:
        if team == dice.team:
            dice.value = character_roll
        else:
            dice.value = target_roll 

def draw_dice():
    for dice in all_dice:
        if dice.value != None:
            dice.image = all_dice_images[dice.value]
            dice.draw()