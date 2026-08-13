import pygame
import consts

state= {
        "is_window_open": True,
        "is_on_boom": False,
        ""



        }


def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif state["state"] != consts.RUNNING_STATE:
            continue

