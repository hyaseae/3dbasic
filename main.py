import pygame, sys
from pygame import Surface
from scenes.home import HomeScene
from scenes.ingame import IngameScene
from scenes.home import SCENE_NAME as HOME_SCENE_NAME
from scenes.ingame import SCENE_NAME as INGAME_SCENE_NAME
from gamebasic.signal.signal import FormalSignals
from gamebasic.objects.state import GameState
from gamebasic.objects.runtime import RunTimeContext
from gamebasic.io.write import save_game

DEBUG = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def init_() -> Surface:

    pygame.init()
    pygame.display.set_caption("Game")
    return pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def main():
    clock = pygame.time.Clock()
    game_state = GameState()
    runtime = RunTimeContext(game_state)
    signal_bus = runtime.signal_bus
    scene_manager = runtime.scene_manager

    scene_manager.register(HOME_SCENE_NAME, HomeScene)
    scene_manager.register(INGAME_SCENE_NAME, IngameScene)
    scene_manager.change_scene(game_state.current_scene_name)

    while True:
        # signal handling

        if signal_bus.check(FormalSignals.NEXT_SCENE.value):
            next_name:str = signal_bus.pop(FormalSignals.NEXT_SCENE.value).get_strdata()
            scene_manager.change_scene(next_name)

        if signal_bus.check(FormalSignals.EXIT_GAME.value):
            # exiting game

            # saving game
            save_game(runtime.game_state)

            # break loop.
            break

        # scene ticking.
        scene_manager.tick(screen=screen)

        # applying display
        pygame.display.flip()
        
        clock.tick(FPS)


        # event handling, for some wierd cases that scene does not handles.
        pygame.event.pump()

if __name__ == "__main__":
    # for testing this, note that this is working on .venv.
    screen = init_()
    main()
    pygame.quit()
    sys.exit()