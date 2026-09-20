"""
ingame scene.
"""

SCENE_NAME = "INGAME"


from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus

class IngameScene(Scene):
    def __init__(
        self,
        game_state: GameState,
        option: OptionData,
        signal_bus: SignalBus,
    ) -> None:
        super().__init__(game_state, option, signal_bus)
        self.canvas = canvas()

    def update(self) -> bool:
        return False

    def render(self, screen) -> None:
        self.canvas.render(screen)