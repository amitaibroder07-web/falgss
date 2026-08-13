import pygame
import consts
import screen

state = {
    "is_window_open": True,
    "is_on_boom": False,
    "state": consts.RUNNING_STATE,

}


def main():
    pygame.init()
    pass


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
