"""
Scene manager.
"""

from gamebasic.objects.scene import Scene
from gamebasic.objects.dataclasses.game_context import GameContext

class SceneManager:
    def __init__(
        self,
        context:GameContext
    ) -> None:
        self.context = context
        self.current_scene: Scene | None = None
        self._factories = {}

    def register(self, name:str, factory:type[Scene]) -> None:
        self._factories[name] = factory

    def change_scene(self, name:str) -> None:
        if name not in self._factories:
            raise KeyError(f"uncorrect scene name : {name}")
        factory = self._factories[name]
        self.context.game_state.current_scene_name = name
        self.current_scene = factory(self.context)

    def tick(self, screen) -> bool:
        if self.current_scene is None:
            raise RuntimeError("No active scene")

        return self.current_scene.tick(screen)