import random
import pygame
import game_field
import consts
import main
soldier_matrix=""
def create_soldier_body():
        global soldier_matrix
        soldier_matrix = game_field.create_matrix()
        # רגליים
        for row in range(3, 4):
            for col in range(2):
                soldier_matrix[row][col] = consts.leg
        # גוף עליון
        for row in range(3):
            for col in range(2):
                soldier_matrix[row][col] = consts.body
        return soldier_matrix
  #"is_window_open": True,
   # "is_on_boom": False,
    #"state": consts.RUNNING_STATE,
    #"pressed_enter": False,
    #"moved_right": False,
    #"moved_left": False,
    #"moved_up": False,
    #"moved_down": False,
def get_soldier_location(up,down,left,right):
    global soldier_matrix
    for row in range(len(soldier_matrix)-1,0,-1):
        for col in range(49,0,-1):
            if soldier_matrix[row][col] == consts.leg:
                if right:
                    soldier_matrix[row][col] = consts.leg
                    for num in range(4):
                        soldier_matrix[row-num][col-1] = ''
                        soldier_matrix[row-num][col + 1] = consts.body
                    soldier_matrix[row][col + 1] = consts.leg


                elif down:
                    soldier_matrix[row+1][col-1] = consts.leg
                    soldier_matrix[row +1][col] = consts.leg
                    soldier_matrix[row][col] = consts.body
                    soldier_matrix[row][col-1] = consts.body
                    soldier_matrix[row-3][col] =''
                    soldier_matrix[row - 3][col-1] = ''

    for row in range(len(soldier_matrix)):
        for col in range(49):
            if soldier_matrix[row][col] == consts.leg:
                if left:
                    for num in range(4):
                        soldier_matrix[row-num][col+1]=''
                        soldier_matrix[row-num][col-1] = consts.body
                        soldier_matrix[row][col - 1] = consts.leg

                elif up:
                    soldier_matrix[row][col] = ''
                    soldier_matrix[row -1][col] = consts.leg
                    soldier_matrix[row-4][col] = consts.body








    pass


def soldier_touch_flag(flag_location):
    pass


def soldier_touch_bomb(bomb):
    pass







#game_field.matrix_of_screen