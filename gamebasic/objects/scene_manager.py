"""
Scene manager.
"""

from gamebasic.objects.scene import Scene
from gamebasic.objects.state import GameState
from gamebasic.signal.signal_bus import SignalBus

class SceneManager:
    def __init__(self, game_state:GameState, signal_bus:SignalBus) -> None:
        self.game_state:GameState = game_state
        self.signal_bus:SignalBus = signal_bus
        self.current_scene: Scene | None = None
        self._factories = {}

    def register(self, name:str, factory:type[Scene]) -> None:
        self._factories[name] = factory

    def change_scene(self, name:str) -> None:
        if name not in self._factories:
            raise KeyError(f"uncorrect scene name : {name}")
        factory = self._factories[name]
        self.game_state.current_scene_name = name
        self.current_scene = factory(self.game_state, self.signal_bus)

    def tick(self, screen) -> bool:
        if self.current_scene is None:
            raise RuntimeError("No active scene")

        return self.current_scene.tick(screen)