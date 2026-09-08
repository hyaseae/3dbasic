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
    DATA = auto()

class FormalSignals(Enum):
    """
    some formal signals to make smart filling work.
    """
    EXIT_GAME = "EXIT_SIGNAL"
    NEXT_SCENE = "NEXT_SCENE"

class Signal():
    """
    signals idead by godot engine.
    """
    signal_count = 0
    def __init__(self, signal_type: SignalType = SignalType.NONE, data: None | str | int | float = None, signal_name:str = "") -> None:

        self.type:SignalType = SignalType.NONE
        self.data: object = None
        self.strdata: str = ""
        def err_func():
            raise NotImplementedError()
        self.executable: Callable = err_func
        self.name:str = ""
        self.closed:bool = False
        self.numdata: int|float = 0
        self.booldata:bool = False

        # really sets data from signal type

        if (signal_type == SignalType.STR and isinstance(data, str)):
            self.strdata = data
        elif (signal_type == SignalType.INT or signal_type == SignalType.FLOAT) and isinstance(data, (int, float)):
            self.numdata = data
        elif (signal_type == SignalType.FUNCTION and isinstance(data, Callable)):
            self.executable = data
        elif (signal_type == SignalType.BOOL and isinstance(data, bool)):
            self.booldata = data
        elif (signal_type == SignalType.DATA):
            self.data = data
        else:
            # type mismatch here
            self.data = data
            raise TypeError("Signal's type is uncorrectly set.")


                

    def get_strdata(self) -> str:
        """
        returns string data.
        """
        return self.strdata

    def get_numdata(self) -> int | float:
        """
        returns numeric data.
        """
        return self.numdata


    def get_data(self) -> object:
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

    def set_signal_name_automatically(self) -> None:
        """
        sets signal name automatically, using signal count.
        """
        self.name = str(self.get_signal_count())
        return

    @classmethod
    def get_signal_count(cls) -> int:
        """
        get signal count that autoincements after getting one.
        """
        cls.signal_count += 1
        return cls.signal_count