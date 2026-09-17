"""
home scene for game starting.
"""

from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.state import GameState
from gamebasic.signal.signal_bus import SignalBus

SCENE_NAME = "HOME"

class HomeScene(Scene):
    def __init__(self, game_state:GameState, signal_bus:SignalBus) -> None:
        super().__init__(game_state, signal_bus)
        self.canvas = canvas(800, 600)

    def update(self) -> bool:
        return False

    def render(self, screen):
        self.canvas.render(screen)
