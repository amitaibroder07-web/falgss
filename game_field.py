from queue import Queue
import copy
import consts
import random
import soldier

game_matrix = ""


def create_matrix():
    global game_matrix
    game_matrix = [50 * [i for i in " "] for j in range(25)]
    return game_matrix


def flag_placement():
    global game_matrix
    create_matrix()
    for row in range(21, 24):
        for col in range(46, 50):
            game_matrix[row][col] = consts.flag


def leg_placement():
    global game_matrix
    flag_placement()
    for row in range(3, 4):
        for col in range(2):
            game_matrix[row][col] = consts.leg


def upper_body():
    global game_matrix
    leg_placement()
    for row in range(3):
        for col in range(2):
            game_matrix[row][col] = consts.body


def bomb_placement():
    global game_matrix
    upper_body()
    for boom in range(20):
        while True:
            row = random.randint(0, 24)
            col = random.randint(0, 47)
            empty_slots = all(game_matrix[row][col + i] == ' ' for i in range(3)) and game_matrix[row][col -1] != "b"
            if game_matrix[row][col] == consts.bomb:
                continue
            elif empty_slots:
                for i in range(3):
                    game_matrix[row][col + i] = consts.bomb
            else:
                continue
            break
    return game_matrix


def display_matrix(matrix):
    for row in matrix:
        print(row)

def get_matrix():
    bomb_placement()
    return copy.deepcopy(game_matrix)

now_game_matrix=get_matrix()


def is_dead(game_matrix):
    for row in range(len(game_matrix)):
        for col in range(len(game_matrix[row])):
            if soldier.soldier_matrix[row][col] == consts.leg and game_matrix[row][col] == consts.bomb:
                return True


def is_win(game_matrix):

    for row in range(len(game_matrix)):
        for col in range(len(game_matrix[row])):
            if soldier.soldier_matrix[row][col] == consts.body and game_matrix[row][col] == consts.flag:
                return True



def get_bomb_location(game_matrix):
    bomb_locations=[]
    for row in range(len(game_matrix)):

        for col in range(len(game_matrix[row])-2):
            if all(game_matrix[row][col + i] == 'b' for i in range(3)):
                bomb_locations.append((row,col))

    return bomb_locations

