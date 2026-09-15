"""
Scene manager.
"""

from gamebasic.objects.scene import Scene
from gamebasic.objects.state import GameState

class SceneManager:
    def __init__(self, game_state:GameState) -> None:
        self.game_state:GameState = game_state
        self.current_scene: Scene | None = None
        self._factories = {}

    def register(self, name:str, factory) -> None:
        self._factories[name] = factory

    def change_scene(self, name:str) -> None:
        factory = self._factories[name]
        self.current_scene = factory(self.game_state)

    def tick(self, screen) -> bool:
        if self.current_scene is None:
            raise RuntimeError("No active scene")

        return self.current_scene.tick(screen)