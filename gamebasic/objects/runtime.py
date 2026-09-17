from gamebasic.objects.state import GameState
from gamebasic.signal.signal_bus import SignalBus
from gamebasic.objects.scene_manager import SceneManager
from gamebasic.debug.logging import LOG

class RunTimeContext():
    def __init__(self, game_state : GameState) -> None:
        self.game_state = game_state
        self.signal_bus = SignalBus()
        self.scene_manager = SceneManager(game_state, self.signal_bus)
        self.log = LOG()