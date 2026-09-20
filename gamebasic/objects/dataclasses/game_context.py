from dataclasses import dataclass
from gamebasic.objects.dataclasses.state import GameState
from gamebasic.objects.dataclasses.option import OptionData
from gamebasic.signal.signal_bus import SignalBus




@dataclass
class GameContext:
    game_state: GameState
    option: OptionData
    signal_bus: SignalBus