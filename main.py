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


def main():
    pygame.init()
    soldiers=pygame.rect(0,0,consts.soldier_height,consts.soldier_width)

    clock = pygame.time.Clock()
    while state["is_window_open"]:
        clock.tick(consts.FPS)
        handle_user_events()

        Screen.draw_game(state)


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                pass


def is_win():
    pass


def is_lose():
    pass


if __name__ == "__main__":
    main()
