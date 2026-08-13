import pygame
import consts
import main
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
soldier_img = pygame.image.load("soldier.png")
soldier_night_img = pygame.image.load("soldier_nigth.png")
soldier = pygame.transform.scale(soldier_img, (consts.soldier_height,consts.soldier_width))
soldier_night = pygame.transform.scale(soldier_night_img, (consts.soldier_height,consts.soldier_width))


def change_screen(val,game_state):
    if val:
        screen.fill(consts.BACKGROUND_COLOR2)
        screen.blit(soldier_night, (game_state.x, game_state.y))
        pygame.display.update()
        pygame.time.delay(1000)



def create_bombs(bomb_img):
    bombs = pygame.image.load(bomb_img)


def draw_bombs(bomb):
    pass

def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)

    screen.blit(soldier, (game_state.x, game_state.y) )



    pygame.display.update()


