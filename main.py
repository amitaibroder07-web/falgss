import pygame
import consts
import Screen


state = {
    "is_window_open": True,
    "is_on_boom": False,
    "state": consts.RUNNING_STATE,
    "pressed_enter": False,
}

pygame.display.set_caption("capture the flag!")

man = pygame.Rect(0,0,consts.soldier_width,consts.soldier_height)
def main():
    pygame.init()
    clock = pygame.time.Clock()
    while state["is_window_open"]:
        clock.tick(consts.FPS)
        handle_user_events(man)



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
            if event.key == pygame.K_UP and man.y- consts.move_length >0-consts.soldier_height*0.5 :
                man.y-=consts.move_length
            if event.key == pygame.K_RIGHT and man.x+ consts.move_length <consts.WINDOW_WIDTH- consts.soldier_width*0.25:
                man.x+=consts.move_length
            if event.key == pygame.K_LEFT and man.x- consts.move_length >0 - consts.soldier_width*0.25 :
                man.x-=consts.move_length
            if event.key==pygame.K_RETURN:
                state["pressed_enter"] = True


def is_win():
    pass


def is_lose():
    pass


if __name__ == "__main__":
    main()
