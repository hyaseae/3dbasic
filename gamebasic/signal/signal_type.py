from enum import Enum, auto

class SignalType(Enum):
    """
    sample signal types enum. maybe extended.
    """
    NONE = auto()
    STR = auto()
    INT = auto()
    FLOAT = auto()
    FUNCTION = auto()
    BOOL = auto()
    DATA = auto()