import pygame, sys
from pygame import Surface
from scenes.home import main as home_main
from gamebasic.objects.scene import Scene
from scenes.home import SCENE_NAME as HOME_SCENE_NAME
from gamebasic.objects.signal import FormalSignals

clock = pygame.time.Clock()

scene = Scene()

SCENES_FUNCTIONS = {
    HOME_SCENE_NAME: home_main,
    
}

#variables

DEBUG = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


# game inits.

def init_() -> None:
    scene.log.add_msg("initiating")
    # init tasks
    scene.set_current_scene_name(HOME_SCENE_NAME)
    scene.set_current_scene_func(home_main)
    pygame.init()
    pygame.display.set_caption("Game")

    # init ended
    scene.log.add_msg("initialized")

def main():
    while True:
        # scene change
        change_scene, changing_scene_name = scene.current_scene()
        if change_scene:
            scene.set_current_scene_name(changing_scene_name)
            scene.set_current_scene_func(SCENES_FUNCTIONS[changing_scene_name])

        # signal handling
        if scene.check_signal(FormalSignals.EXIT_GAME.value):
            # exiting game

            scene.log.add_msg("saving...")
            # save game

            scene.log.add_msg("saved!")

            if DEBUG:
                scene.log.print_by_level(file_output=True)

            scene.log.clear_log()
            # break loop.
            break

        clock.tick(FPS)


if __name__ == "__main__":
    scene.log.add_msg("started")
    init_()
    main()
    pygame.quit()
    sys.exit()