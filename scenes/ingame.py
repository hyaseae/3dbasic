"""
ingame scene.
"""

SCENE_NAME = "INGAME"


from gamebasic.objects.UI.canvas import canvas
from gamebasic.objects.scene import Scene
from gamebasic.objects.state import GameState

class IngameScene(Scene):
    def __init__(self, game_state: GameState) -> None:
        self.game_state = game_state
        self.canvas = canvas(800, 600)

    def update(self) -> bool:
        return False

    def render(self, screen) -> None:
        self.canvas.render(screen)