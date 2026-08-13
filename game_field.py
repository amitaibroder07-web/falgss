import consts
import random


game_matrix=""
def create_matrix():
    global game_matrix
    game_matrix = [50*[i for i in " "]for j in range(25)]
    return game_matrix



def bomb_placement():
    global game_matrix
    create_matrix()
    spawn_soldier = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[3,0],[3,1]]
    for boom in range(20):
        while True:
            row = random.randint(0,24)
            col = random.randint(0,47)
            empty_slots = all(map(lambda num: " " == game_matrix[row][col] == num == game_matrix[row][col + 2],game_matrix[row]))
            if game_matrix[row][col] == consts.bomb:
                continue
            elif [row,col] in spawn_soldier:
                continue
            elif empty_slots:
                for i in range(3):
                    game_matrix[row][col+i]=consts.bomb
            else:
                continue
            break
    return game_matrix









def flag_placement():
    pass