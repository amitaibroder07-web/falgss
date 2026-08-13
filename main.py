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
def draw_game(game_state):
    Screen.screen.fill(consts.BACKGROUND_COLOR)

    Screen.screen.blit(Screen.soldier, (game_state.x, game_state.y) )



    pygame.display.update()

def main():
    pygame.init()
    man = pygame.Rect(0,0,consts.soldier_width,consts.soldier_height)
    clock = pygame.time.Clock()
    while state["is_window_open"]:
        clock.tick(consts.FPS)
        handle_user_events(man)

        draw_game(man)


def handle_user_events(man):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False


        elif state["state"] != consts.RUNNING_STATE:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                man.y+=consts.move_length
            if event.key == pygame.K_UP:
                man.y-=consts.move_length
            if event.key == pygame.K_RIGHT:
                man.x+=consts.move_length
            if event.key == pygame.K_LEFT:
                man.x-=consts.move_length


def is_win():
    pass


def is_lose():
    pass


if __name__ == "__main__":
    main()
