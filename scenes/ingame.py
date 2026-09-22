"""
ingame scene.
"""

SCENE_NAME = "INGAME"


from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus
from gamebasic.objects.dataclasses.game_context import GameContext
from gamebasic.objects.UI.img import load_cached_img
from os.path import join as jr
from threeDbasic.objects.camera import Camera3D

IMG_ASSETS_FOLDER = jr("assets", "UI")

class IngameScene(Scene):
    def __init__(
        self,
        context : GameContext
    ) -> None:
        super().__init__(context)
        self.canvas = canvas(load_cached_img(jr(IMG_ASSETS_FOLDER, "background.png")),
                        context.option.screen_width, 
                        context.option.screen_height)

        self.ui_setup()
        self.camera = Camera3D()

    def ui_setup(self):
        pass

    def update(self) -> bool:
        return False

    def render(self, screen) -> None:
        self.canvas.render(screen)

    def event(self):
        pass