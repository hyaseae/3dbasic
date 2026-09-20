import pygame, sys
from pygame import Surface
from scenes.home import HomeScene
from scenes.ingame import IngameScene
from scenes.option import OptionScene
from scenes.home import SCENE_NAME as HOME_SCENE_NAME
from scenes.ingame import SCENE_NAME as INGAME_SCENE_NAME
from scenes.option import SCENE_NAME as OPTION_SCENE_NAME
from gamebasic.signal.signal import FormalSignals
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.runtime import RunTimeContext
from gamebasic.io.write import save_game
from gamebasic.io.read import load_option
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.objects.dataclasses.game_context import GameContext
from gamebasic.signal.signal_bus import SignalBus


def init_() -> OptionData:

    pygame.init()
    pygame.display.set_caption("Game")
    option = load_option()
    return option

def main(option: OptionData, screen: Surface):
    clock = pygame.time.Clock()

    context = GameContext(
        game_state=GameState(),
        option=load_option(),
        signal_bus=SignalBus()
    )
    runtime = RunTimeContext(context)
    signal_bus = runtime.signal_bus
    scene_manager = runtime.scene_manager


    #maintaining current scenes
    scene_manager.register(HOME_SCENE_NAME, HomeScene)
    scene_manager.register(INGAME_SCENE_NAME, IngameScene)
    scene_manager.register(OPTION_SCENE_NAME, OptionScene)
    scene_manager.change_scene(context.game_state.current_scene_name)

    while True:
        # signal handling

        if signal_bus.check(FormalSignals.NEXT_SCENE.value):
            next_name:str = signal_bus.pop(FormalSignals.NEXT_SCENE.value).get_strdata()
            scene_manager.change_scene(next_name)

        if signal_bus.check(FormalSignals.EXIT_GAME.value):
            # exiting game

            # saving game
            save_game(runtime.game_state, runtime.game_state.save_file_name)

            # break loop.
            break

        # scene ticking.
        scene_manager.tick(screen=screen)

        # applying display
        pygame.display.flip()
        
        clock.tick(option.FPS)


        # event handling, for some wierd cases that scene does not handles.
        pygame.event.pump()

if __name__ == "__main__":
    # for testing this, note that this is working on .venv.
    option = init_()
    screen = pygame.display.set_mode((option.screen_width,option.screen_height))
    main(option, screen)
    pygame.quit()
    sys.exit()