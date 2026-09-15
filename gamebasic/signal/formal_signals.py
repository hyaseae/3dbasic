from enum import Enum, auto
class FormalSignals(Enum):
    """
    some formal signals to make smart filling work.
    """
    EXIT_GAME = "EXIT_SIGNAL"
    NEXT_SCENE = "NEXT_SCENE"