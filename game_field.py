import consts
import random


game_matrix=""
def create_matrix():
    global game_matrix
    game_matrix = [50*[i for i in " "]for j in range(25)]
    return game_matrix

def flag_placement():
    global game_matrix
    create_matrix()
    for row in range(21,24):
        for col in range(46,50):
            game_matrix[row][col]=consts.flag

def bomb_placement():
    global game_matrix
    flag_placement()
    dont_spawn = [[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[3,0],[3,1],[21,46],[21,47],[21,48],[21,49],
                  [22,46],[22,47],[22,48],[22,49],[23,46],[23,47],[23,48],[23,49]]
    for boom in range(20):
        while True:
            row = random.randint(0,24)
            col = random.randint(0,47)
            empty_slots = all(map(lambda num: " " == game_matrix[row][col] == num == game_matrix[row][col + 2],game_matrix[row]))
            if game_matrix[row][col] == consts.bomb:
                continue
            elif [row,col] in dont_spawn:
                continue
            elif empty_slots:
                for i in range(3):
                    game_matrix[row][col+i]=consts.bomb
            else:
                continue
            break
    return game_matrix











