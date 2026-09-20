from gamebasic.objects.dataclasses.state import GameState
from gamebasic.signal.signal_bus import SignalBus
from gamebasic.objects.scene_manager import SceneManager
from gamebasic.debug.logging import LOG
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.objects.dataclasses.game_context import GameContext

class RunTimeContext():
    """
    managing everything in ram in main.
    """
    def __init__(self, context:GameContext) -> None:
        self.game_state = context.game_state
        self.option = context.option
        self.signal_bus = context.signal_bus
        self.scene_manager = SceneManager(context)
        self.log = LOG()