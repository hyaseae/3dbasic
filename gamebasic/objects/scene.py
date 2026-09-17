"""
scene's abstract class
"""
from gamebasic.debug.logging import LOG
from gamebasic.objects.state import GameState
from gamebasic.signal.signal_bus import SignalBus

class Scene():
    """
    scene class that gets global datas.
    maybe used in save things?
    """
    def __init__(self, game_state:GameState, signal_bus:SignalBus) -> None:
        self.log = LOG()
        self.game_state:GameState = game_state
        self.signal_bus:SignalBus = signal_bus

    def tick(self, screen) -> bool:
        """
        updates and renders scene.
        """
        changed:bool = self.update()
        self.render(screen)
        return changed

    def update(self) -> bool:
        """
        handle events, check scene changes and more.
        """
        raise NotImplementedError()
        

    def render(self, screen):
        """
        renders the scene.
        """
        raise NotImplementedError()