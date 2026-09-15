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
        return super().update()

    def render(self, screen):
        return super().render(screen)

    def tick(self, screen) -> bool:
        # 입력 처리 및 상태 변경
        self.canvas.render(screen)

        return False