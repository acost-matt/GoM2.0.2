
import pygame
from constants import *
from board import *

all_characters = pygame.sprite.Group()
selected_character = pygame.sprite.GroupSingle()
characters_on_board = pygame.sprite.Group()
team_true = pygame.sprite.Group()
team_false = pygame.sprite.Group()

class Character(pygame.sprite.Sprite):
    def __init__(self, image, rect, level, health):
        super().__init__()
        self.image = image
        self.rect = rect
        self.level = level
        self.health = health
        self.is_selected = False
        self.on_board = False
        self.is_king = False
        self.team = False
        self.space = None

    def __repr__(self):
        rep = str(self.rect) + str( self.level) + str( self.health)
        return rep

    def draw():
        all_characters.draw(SCREEN)

    def draw_teams():
        characters_on_board.draw(SCREEN)
        

    def select(self):
        self.is_selected = True
        all_characters.remove(self)
        characters_on_board.remove(self)
        selected_character.add(self)

    def drag(self, x, y):
        self.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = x, y

    def place(self, rect, space):
        self.rect = rect
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)
        self.space = space
    
    def reset(self):
        self.rect = self.space.rect

class Brute(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Brute" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = BRUTERECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves

    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) == 1 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) == 1 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks


class Cannon(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Cannon" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = CANNONRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)
    
    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 2 and abs(space.col - start.col) <= 1:
                        attacks.append(space.rect)
                    elif abs(space.col - start.col) <= 2 and abs(space.row - start.row) <= 1:
                        attacks.append(space.rect)
        return attacks   

class Archer(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Archer" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = ARCHERRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Boxer(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Boxer" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = BOXERRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) ==1 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) == 1 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Support(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Support" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = SUPPORTRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) == 1 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) == 1 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Diagonal(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Diagonal" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = DIAGONALRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) <= 2 or abs(space.row - start.row) <= 2:
                    if abs(space.col - start.col) == abs(space.row - start.row) and space.col != start.col:
                        moves.append(space.rect)
                    elif abs(space.row - start.row) == abs(space.col - start.col) and space.col != start.col:
                        moves.append(space.rect)
                    elif abs(space.col - start.col) == 1 and space.row == start.row:
                        moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Mimic(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Mimic" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = MIMICRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Ninja(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Ninja" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = NINJARECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Transporter(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Transporter" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = TRANSPORTERRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

class Commoner(Character):
    def __init__(self, image, rect, level, health):
        super().__init__(image, rect, level, health)

    def __repr__(self):
        rep = "Commoner" + str(self.rect) + str( self.level) + str( self.health) + str(self.team) + str(self.is_king)
        return rep
    
    def get_rect(self):
        self.rect = COMMONERRECT
        self.is_selected = False
        selected_character.empty()
        all_characters.add(self)

    def valid_moves(self):
        moves = []
        start = self.space
        for space in all_spaces:
            if space.filled == False:
                if abs(space.col - start.col) == 1 and space.row == start.row:
                    moves.append(space.rect)
                elif abs(space.row - start.row) == 1 and space.col == start.col:
                    moves.append(space.rect)
        return moves
    
    def valid_attack(self):
        attacks = []
        start = self.space
        for space in all_spaces:
            if space.filled:
                if space.team != self.team:
                    if abs(space.col - start.col) <= 3 and space.row == start.row:
                        attacks.append(space.rect)
                    elif abs(space.row - start.row) <= 3 and space.col == start.col:
                        attacks.append(space.rect)
        return attacks

def create_all_characters():
    all_characters.empty()
    all_characters.add(Brute(BRUTEIMAGE, BRUTERECT, 4, 3))
    all_characters.add(Cannon(CANNONIMAGE, CANNONRECT, 4, 3))
    all_characters.add(Archer(ARCHERIMAGE, ARCHERRECT, 3, 2))
    all_characters.add(Boxer(BOXERIMAGE, BOXERRECT, 3, 3))
    all_characters.add(Support(SUPPORTIMAGE, SUPPORTRECT, 3, 2))
    all_characters.add(Diagonal(DIAGONALIMAGE, DIAGONALRECT, 2, 1))
    all_characters.add(Mimic(MIMICIMAGE, MIMICRECT, 2, 1))
    all_characters.add(Ninja(NINJAIMAGE, NINJARECT, 2, 1))
    all_characters.add(Transporter(TRANSPORTERIMAGE, TRANSPORTERRECT, 2, 1))
    all_characters.add(Commoner(COMMONERIMAGE, COMMONERRECT, 1, 1))

def remove_dead():
    for character in characters_on_board:
        if character.health == 0:
            for space in all_spaces:
                if character.space.col == space.col and character.space.row == space.row:
                    space.team = None
            characters_on_board.remove(character)
            characters_on_board.update()
        
