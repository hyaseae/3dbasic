from enum import Enum, auto
from collections.abc import Callable

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

class FormalSignals(Enum):
    """
    some formal signals to make smart filling work.
    """
    EXIT_GAME = "EXIT_SIGNAL"

class Signal():
    """
    signals idead by godot engine.
    """
    signal_count = 0
    def __init__(self) -> None:
        self.type:SignalType = SignalType.NONE
        self.data: int|float|str|bool|None = None
        def err_func():
            raise NotImplementedError()
        self.executable: Callable = err_func
        self.name:str = ""
        self.closed:bool = False

    def get_data(self):
        """
        if type is str, int or data-like type, use this function.
        or, just to get data attached to function, use this function.
        """
        return self.data

    def executeable(self):
        """
        returns the inner function itself.
        """
        return self.executable

    def execute(self):
        """
        executes inner function itself... Will It Be Reallllly Useful??
        """
        return self.executable()

    def close_signal(self):
        """
        close signal itself.
        btw, closed signals should always be deleted manually.
        """
        self.closed = True
        return

    def get_signal_name(self):
        """
        get signal's name
        """
        return self.name

    def set_signal_name(self, name):
        """
        sets signal's name
        """
        self.name = name
        return

    @classmethod
    def get_signal_count(cls) -> int:
        """
        get signal count that autoincements after getting one.
        """
        cls.signal_count += 1
        return cls.signal_count