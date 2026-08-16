from queue import Queue
import copy
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
def leg_placement():
    global game_matrix
    flag_placement()
    for row in range(3,4):
        for col in range(2):
            game_matrix[row][col]=consts.leg
def bomb_placement():
    global game_matrix
    leg_placement()
    for boom in range(20):
        while True:
            row = random.randint(0,24)
            col = random.randint(0,47)
            empty_slots = all(game_matrix[row][col+i]==' 'for i in range(3))
            if game_matrix[row][col] == consts.bomb:
                continue
            elif empty_slots:
                for i in range(3):
                    game_matrix[row][col+i]=consts.bomb
            else:
                continue
            break


    return game_matrix



def display_matrix(matrix):
    matrix_row=''
    for row in matrix:
        for col in row:
            matrix_row+=' '+ col
        print(matrix_row)
        matrix_row = ''

#יש אופציה לכך שהפצצות יחסמו את הדרך לדגל כך שהשחקן לא יוכל להגיע ויפסיד אוטומטית
#התייחסתי למקרה קצה הזה והשתמשתי בpathfinder ככה שבמקרה ולא יהיה דרך אחרי הפצצות אנחנו נכין מפה חדשה
def dictpathfinder():
    global game_matrix
    bomb_placement()
    game_matrix_path=copy.deepcopy(game_matrix)

    #סתם קראתי לו דיקט פשוט הייתיח צריך מילון שיחזיק את המשתנים
    dict1 = {}
    matrix_size =len(game_matrix_path)
    row_size = len(game_matrix[0])

    for row in range(matrix_size):
        for col in range(row_size):
            if game_matrix_path[row][col]!=consts.bomb:
                nodes = []
                if row+1 < matrix_size and game_matrix_path[row+1][col] != consts.bomb:#down
                    nodes.append((row+1,col))
                if row-1 >= 0 and game_matrix_path[row-1][col] != consts.bomb:#up
                    nodes.append((row-1,col))
                if col+1 < row_size and game_matrix_path[row][col+1] != consts.bomb: #right
                    nodes.append((row,col+1))
                if col-1 >= 0 and game_matrix_path[row][col-1] != consts.bomb: #left
                    nodes.append((row,col-1))
                dict1[(row,col)] = nodes
    return dict1,game_matrix_path
testing=15
def is_there_way():
    global game_matrix
    dict1,game_matrix_path = dictpathfinder()
#אנחנו מחפשים את הדרך הקצרה ביותר(ככה נתמודד עם מקרה הקצה לכן נבדוק אם היינו שם או לא

    start = (3, 1)
    werethere = [start]
    end = (21,46)
    q = Queue()
    q.put([start])

    while not q.empty():
        path = q.get()
        neighbors = dict1[path[-1]]
        for neighbor in neighbors:
            if neighbor == end:
                for cooradinate in path:
                    row,col = cooradinate
                    game_matrix_path[row][col]='W'
                return game_matrix_path
            if neighbor not in werethere:
                werethere.append(neighbor)
                new_path = path + [neighbor]
                q.put(new_path)


def bomb_check():
    global game_matrix
    while True:
        findaway = is_there_way()
        if findaway:
            display_matrix(game_matrix)
            return True
        else:
            bomb_placement()
bomb_check()
t=5+5











