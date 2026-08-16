import pygame
import consts
import Screen
import soldier
import game_field
from game_field import is_dead

state = {
    "is_window_open": True,
    "is_on_boom": False,
    "state": consts.RUNNING_STATE,
    "pressed_enter": False,
    "moved_right": False,
    "moved_left": False,
    "moved_up": False,
    "moved_down": False,
}

pygame.display.set_caption("capture the flag!")

man = pygame.Rect(0,0,consts.soldier_width,consts.soldier_height)
def main():
    soldier.create_soldier_body()
    pygame.init()
    clock = pygame.time.Clock()
    while state["is_window_open"]:
        Screen.draw_flag()
        clock.tick(consts.FPS)
        handle_user_events(man)
        state["moved_down"] = False
        state["moved_up"] = False
        state["moved_right"] = False
        state["moved_left"] = False

        Screen.change_screen(state["pressed_enter"],man)
        state["pressed_enter"] = False



        Screen.draw_game(man)


def handle_user_events(man):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and man.y+ consts.move_length <consts.WINDOW_HEIGHT - consts.soldier_height*1.5:
                man.y+=consts.move_length
                state["moved_down"] = True

            if event.key == pygame.K_UP and man.y- consts.move_length >0-consts.soldier_height*0.5 :
                man.y-=consts.move_length
                state["moved_up"] =True
            if event.key == pygame.K_RIGHT and man.x+ consts.move_length <consts.WINDOW_WIDTH- consts.soldier_width*0.25:
                man.x+=consts.move_length
                state["moved_right"] = True
            if event.key == pygame.K_LEFT and man.x- consts.move_length >0 - consts.soldier_width*0.25 :
                man.x-=consts.move_length
                state["moved_left"] = True
            soldier.get_soldier_location(state["moved_up"],state["moved_down"],state["moved_left"],state["moved_right"])
            if event.key==pygame.K_RETURN:
                state["pressed_enter"] = True
            if game_field.is_win():
                print("gay")








def is_win():
    pass


def is_lose():
    pass


if __name__ == "__main__":
    main()
