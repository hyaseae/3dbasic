"""
home scene for game starting.
"""

from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.state import GameState

SCENE_NAME = "HOME"

class HomeScene(Scene):
    def __init__(self, game_state:GameState) -> None:
        self.game_state:GameState = game_state
        self.canvas = canvas(800, 600)

    def update(self) -> bool:
        return False

    def render(self, screen):
        self.canvas.render(screen)
