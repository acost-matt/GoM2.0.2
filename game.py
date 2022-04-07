import pygame
from characters import *
from board import *
from button import *
from dice import *
from crown import *

game_phase = 0
turn = None
moving = False
attacking = False
powerup = False
stop_dice = False
rolling = False
start_space = None
target_space = None

def run():
    global turn, moving, attacking, powerup, rolling, stop_dice, start_space, target_space
    x, y = pygame.mouse.get_pos()
    mousepressed = pygame.mouse.get_pressed()[0]
    if game_phase == 0:
        SCREEN.fill(BLACK)
        Board.draw_board(Board())
        Character.draw()
        crown.draw()
        selected_character.draw(SCREEN)
        if mousepressed:
            if crown.selected:
                crown.drag(x, y)
            if crown.rect.collidepoint(x, y) and len(selected_character.sprites()) == 0:
                crown.select()
                for character in all_characters:
                    character.is_king = False
            elif len(selected_character.sprites()) == 0 and crown.selected == False:
                    for character in all_characters:
                        if character.rect.collidepoint(x, y):
                            character.select()
                            if character.on_board:
                                index = character.rect.collidelist(all_spaces)
                                space = all_spaces[index]
                                space.filled = False
                            else:
                                continue
                        else:
                            continue

            elif len(selected_character.sprites()) == 1:
                for character in selected_character:
                    character.drag(x, y)
            if sum_levels() == 10 and has_king():
                false_team = create_team_false_button.draw(SCREEN)
                true_team = create_team_true_button.draw(SCREEN)
                if false_team:
                    for character in all_characters:
                        character.team = False
                    for character in characters_on_board:
                        if character.team == False:
                            characters_on_board.remove(character)
                    add_to_board()
                    create_all_characters()
                    clear_board()
                elif true_team:
                    for character in all_characters:
                        character.team = True
                    for character in characters_on_board:
                        if character.team == True:
                            characters_on_board.remove(character)
                    adjust_side()
                    add_to_board()
                    create_all_characters()
                    clear_board()
            if check_ready():
                roll = roll_dice_button.draw(SCREEN)
                if roll:
                    new_phase()

        else:
            if crown.selected:
                crown.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                index = crown.rect.collidelist(all_spaces)
                left, top = crown.rect.topleft
                if index >= 0:
                    space = all_spaces[index]
                    if space.rect.collidepoint(left, top):
                        if space.filled:
                            for character in all_characters:
                                if character.space != None:
                                    if character.space.col == space.col and character.space.row == space.row:
                                        crown.rect = character.rect
                                        crown.character = character
                                        character.is_king = True
                                        crown.selected = False
                                        break
                                    else:
                                        crown.reset()
                        else:
                            crown.reset()
                    else:
                        crown.reset()   
                else:
                    crown.reset()
            if len(selected_character.sprites()) == 1:
                for character in selected_character:
                    character.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                    index = character.rect.collidelist(all_spaces)
                    if index >= 0:
                        space = all_spaces[index]
                        if space.filled == False and space.row == 5:
                            character.place(space.rect, space)
                            space.filled = True
                            character.on_board = True
                            character.team = False
                        else:
                            character.get_rect()
                            character.on_board = False
                            character.space = None
                    else:
                        character.get_rect()
                        character.on_board = False
                        character.space = None
            if sum_levels() == 10 and has_king():
                create_team_false_button.draw(SCREEN)
                pygame.draw.rect(SCREEN, RED, create_team_false_button.rect, 5)
                create_team_true_button.draw(SCREEN)
                pygame.draw.rect(SCREEN, BLUE, create_team_true_button.rect, 5)
            if check_ready():
                roll_dice_button.draw(SCREEN)


    elif game_phase == 1:
        SCREEN.fill(BLACK)
        Board.draw_board(Board())
        if stop_dice == False:
            roll_dice()
            stop_dice_button.draw(SCREEN)
        draw_dice()
        if mousepressed:
            if all_dice[0].value == None or all_dice[0].value == all_dice[1].value:
                if roll_dice_button.rect.collidepoint(x, y):
                    stop_dice = False
                if stop_dice_button.rect.collidepoint(x, y):
                    stop_dice = False
            else:
                if start_game_button.rect.collidepoint(x, y):
                    if all_dice[0].value > all_dice[1].value:
                        turn = all_dice[0].team
                    else:
                        turn = all_dice[1].team
                    new_phase()
                if stop_dice_button.rect.collidepoint(x, y):
                    if all_dice[0].value != None:
                        if all_dice[0].value != all_dice[1].value:
                            stop_dice = True
        else:
            if stop_dice and all_dice[0].value == all_dice[1].value:
                roll_dice_button.draw(SCREEN)
            
            if stop_dice and all_dice[0].value != all_dice[1].value:
                start_game_button.draw(SCREEN)


    elif game_phase == 2:
        turn_phase()
        remove_dead()
        SCREEN.fill(BLACK)
        Board.draw_board(Board())
        Character.draw_teams()
        show_team()
        selected_character.draw(SCREEN)
        moving_button.draw(SCREEN)
        attacking_button.draw(SCREEN)
        powerup_button.draw(SCREEN)
        selected_phase()
        fill_spaces()
        if moving:
            fill_spaces()
            if mousepressed:
                if len(selected_character.sprites()) == 0:
                    for character in characters_on_board:
                        if character.rect.collidepoint(x, y) and character.team == turn:
                            character.select()
                            index = character.rect.collidelist(all_spaces)
                            space = all_spaces[index]
                            space.filled = False

                elif len(selected_character.sprites()) == 1:
                    for character in selected_character:
                        character.drag(x, y)
                        for space in all_spaces:
                            if space.rect.collidelist(character.valid_moves()) >= 0:
                                if turn:
                                    space.color = BLUE
                                else:
                                    space.color = RED
            else:
                if len(selected_character.sprites()) == 1:
                    for character in selected_character:
                        character.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                        start = character.space.rect
                        index = character.rect.collidelist(all_spaces)
                        if index >= 0:
                            if all_spaces[index].rect.collidelist(character.valid_moves()) >= 0:
                                target = all_spaces[index]
                                if target.filled == False and target.rect != start:
                                    character.rect = target.rect
                                    character.space = target
                                    character.is_selected = False
                                    characters_on_board.add(character)
                                    selected_character.empty()
                                    reset_color()
                                    turn = not turn
                                else:
                                    return_character(character, start)
                            else:
                                return_character(character, start)
                        else:
                            return_character(character, start)
        if attacking:
            fill_spaces()
            if mousepressed:
                if len(selected_character.sprites()) == 0:
                    for character in characters_on_board:
                        if character.rect.collidepoint(x, y) and character.team == turn:
                            character.select()
                            start_space = character.space
                elif len(selected_character.sprites()) == 1:
                    for characters in selected_character:
                        characters.drag(x, y)
                        for space in all_spaces:
                            if space.rect.collidelist(characters.valid_attack()) >= 0:
                                if turn:
                                    space.color = BLUE
                                    space.draw()
                                    selected_character.draw(SCREEN)
                                else:
                                    space.color = RED
                                    space.draw()
                                    selected_character.draw(SCREEN)
                if rolling:
                    if stop_dice_button.draw(SCREEN) and all_dice[0].value != all_dice[1].value:
                        if all_dice[0].value > all_dice[1].value:
                            if find_character(start_space).team == all_dice[0].team:
                                find_character(target_space).health -= 1
                            else:
                                find_character(start_space).health -= 1
                            turn = not turn
                            fill_spaces()
                            rolling = False
                        elif all_dice[1].value > all_dice[0].value:
                            if find_character(start_space).team == all_dice[1].team:
                                find_character(target_space).health -= 1
                            else:
                                find_character(start_space).health -= 1
                            turn = not turn
                            fill_spaces()
                            rolling = False
            
            else:
                draw_dice()
                reset_color()
                if rolling:
                    roll_dice()
                    if stop_dice_button.draw(SCREEN):
                        rolling = False
                for character in selected_character:
                    start_space = character.space
                    if character.rect.collidelist(character.valid_attack()) >= 0:
                        rolling = True
                        character.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                        index = character.rect.collidelist(all_spaces)
                        target_space = all_spaces[index]
                        character.rect = character.space.rect
                        character.is_selected = False
                        selected_character.empty()
                        characters_on_board.add(character)

        
                

def sum_levels():
    levels = 0
    for character in all_characters:
        if character.on_board:
            levels += character.level

    return levels

def adjust_side():
    for character in all_characters:
        if character.on_board:
            col = (character.rect[0] - BOARDSTART[0]) / SQUARE_SIZE
            new_col = abs((col + 1) - COLS)
            for space in all_spaces:
                if space.col == new_col and space.row == 0:
                    character.rect = space.rect
                    character.space = space

def add_to_board():
    for character in all_characters:
        if character.on_board:
            characters_on_board.add(character)

def new_phase():
    global game_phase
    game_phase += 1

def clear_board():
    for space in all_spaces:
        space.filled = False
        crown.reset()

def fill_spaces():
    for character in characters_on_board:
        for space in all_spaces:
            if character.space.col == space.col and character.space.row == space.row:
                space.filled = True
                space.team = character.team
                character.space = space
            else:
                space.filled = False
                space.team = None

def return_character(character, start):
    character.rect = start
    character.is_selected = False
    selected_character.empty()
    characters_on_board.add(character)
    reset_color()

def turn_phase():
    mousepressed = pygame.mouse.get_pressed()[0]
    x, y = pygame.mouse.get_pos()
    global moving, attacking, powerup
    if mousepressed:
        if moving_button.rect.collidepoint(x, y):
            moving = True
            attacking = powerup = False
        if attacking_button.rect.collidepoint(x, y):
            attacking = True
            moving = powerup = False
        if powerup_button.rect.collidepoint(x, y):
            powerup = True
            moving = attacking = False
def selected_phase():
    if turn:
        if moving:
            pygame.draw.rect(SCREEN, BLUE, moving_button.rect, 2, 4)
        if attacking:
            pygame.draw.rect(SCREEN, BLUE, attacking_button.rect, 2, 4)
        if powerup:
            pygame.draw.rect(SCREEN, BLUE, powerup_button.rect, 2, 4)
    else:
        if moving:
            pygame.draw.rect(SCREEN, RED, moving_button.rect, 2, 4)
        if attacking:
            pygame.draw.rect(SCREEN, RED, attacking_button.rect, 2, 4)
        if powerup:
            pygame.draw.rect(SCREEN, RED, powerup_button.rect, 2, 4)

def draw_rect_alpha(surface, color, rect):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
    surface.blit(shape_surf, rect)

def show_team():
    for character in characters_on_board:
        if character.team:
            pygame.draw.rect(SCREEN, BLUE, character.rect, 5)
        else:
            pygame.draw.rect(SCREEN, RED, character.rect, 5)

def find_character(space):
    fill_spaces()
    print(target_space)
    for character in characters_on_board:
        if character.space.col == space.col and character.space.row == space.row:
            return character
        else:
            print("false")

def place_crown(x, y):
    crown.rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
    index = crown.rect.collidelist(all_spaces)
    if index >= 0:
        space = all_spaces[index]
        if space.filled:
            for character in all_characters:
                if character.space != None:
                    if character.space.col == space.col and character.space.row == space.row:
                        crown.rect = character.rect
                        crown.character = character
                        character.is_king = True
                        crown.selected = False
                    else:
                        crown.reset()
        else:
            crown.reset()

    else:
        crown.reset()

def check_ready():
    levels = 0
    for character in characters_on_board:
        levels += character.level
    if levels == 20:
        return True
    else:
        return False

def has_king():
    for character in all_characters:
        if character.is_king:
            return True
            break

def get_battle():
    global start_space, target_space
    return [find_character(start_space), find_character(target_space)]