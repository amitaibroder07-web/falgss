import pygame,time
import consts
import random

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
soldier_img = pygame.image.load("soldier.png")
soldier_night_img = pygame.image.load("soldier_nigth.png")
soldier = pygame.transform.scale(soldier_img, (consts.soldier_height,consts.soldier_width))
soldier_night = pygame.transform.scale(soldier_night_img, (consts.soldier_height,consts.soldier_width))
flag_img = pygame.image.load("flag.png")
flag= pygame.transform.scale(flag_img, (consts.flag_width,consts.flag_height))

def change_screen(val,game_state):
    block=0
    if val:
        screen.fill(consts.BACKGROUND_COLOR2)
        for i in range(consts.NUMBER_OF_BLOCKSY):
            pygame.draw.line(screen,consts.LINE_COLOR,(block,0),(block,consts.WINDOW_HEIGHT))
            block+=consts.move_length
        block=0
        for i in range(consts.NUMBER_OF_BLOCKSX):
            pygame.draw.line(screen,consts.LINE_COLOR,(0,block),(consts.WINDOW_WIDTH,block))
            block+=consts.move_length
        screen.blit(soldier_night, (game_state.x, game_state.y))
        draw_flag()
        pygame.display.update()
        pygame.time.delay(1000)


def draw_bombs(bomb):
    pass

def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)
    screen.blit(soldier, (game_state.x, game_state.y) )
    draw_flag()
    pygame.display.update()

def draw_flag():
    screen.blit(flag,(consts.FLAG_X,consts.FLAG_Y))


def draw_bush():
    for i in range(consts.NUMBER_OF_BUSH):
        pass
