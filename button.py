import pygame
from constants import *

class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

create_team_false_button = Button(1320, 780, CREATETEAMIMAGE, 1)
create_team_true_button = Button(1440, 780, CREATETEAMIMAGE, 1)
roll_dice_button = Button(1320, 240, DIAGONALIMAGE, 1)
stop_dice_button = Button(1320, 780, STOPIMAGE, 1)
start_game_button = Button(1320, 660 , STARTIMAGE, 1)
moving_button = Button(800, 930, NINJAIMAGE, 1)
attacking_button = Button(920, 930, BRUTEIMAGE, 1)
powerup_button = Button(1040, 930, MIMICIMAGE, 1)

