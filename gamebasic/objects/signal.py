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

class Signal():
    """
    signals idead by godot engine.
    """
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