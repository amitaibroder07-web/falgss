import pygame
import consts
import main
screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
soldier_img = pygame.image.load("soldier.png")
soldier = pygame.transform.scale(soldier_img, (consts.soldier_height,consts.soldier_width))
def change_screen():
    pass



def create_bombs(bomb_img):
    bombs = pygame.image.load(bomb_img)


def draw_bombs(bomb):
    pass




def draw_game(game_state):
    screen.fill(consts.BACKGROUND_COLOR)

    screen.blit(soldier, (main.soldiers.x, main.soldiers.y) )



    pygame.display.update()