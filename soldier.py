import random
import pygame
import game_field
import consts
soldier_matrix=""
def create_soldier_body():
        global soldier_matrix
        game_field.bomb_check()
        soldier_matrix = game_field.create_matrix()
        # רגליים
        for row in range(3, 4):
            for col in range(2):
                soldier_matrix[row][col] = consts.leg
        # גוף עליון
        for row in range(3):
            for col in range(2):
                soldier_matrix[row][col] = consts.body

def get_soldier_location(X,Y):
    pass


def soldier_touch_flag(flag_location):
    pass


def soldier_touch_bomb(bomb):
    pass







#game_field.matrix_of_screen