"""
scene's abstract class
"""
from gamebasic.debug.logging import LOG
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus
from gamebasic.objects.dataclasses.game_context import GameContext

class Scene():
    """
    scene class that gets global datas.
    maybe used in save things?
    """
    def __init__(
        self,
        context:GameContext
    ) -> None:
        
        self.log = LOG()
        self.context:GameContext = context
        self.game_state:GameState = context.game_state
        self.option: OptionData = context.option
        self.signal_bus:SignalBus = context.signal_bus

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