"""
total signals for global data transforming
somehow doing global's gob, so just using this.
"""
from enum import Enum, auto
from gamebasic.objects.signal import Signal
from collections.abc import Callable
from gamebasic.debug.logging import LOG


def err_func():
    """ function for err"""
    raise FileNotFoundError()

# conclusion. no use in enums for scene's name. 
# since enum is final and unexpandible, enum is not appropriate for scene names/functions.

class Scene():
    """
    scene class that gets global datas.
    maybe used in save things?
    """
    def __init__(self) -> None:
        self.scene_name:str = "NONE"
        self.current_scene_function = err_func
        self.signal_dict:dict[str, Signal] = {}
        self.log = LOG()

    def get_current_scene_name(self)-> str:
        """
        returns current scene name(str)
        """
        return self.scene_name

    def set_current_scene_name(self, value:str) -> None:
        """
        sets current scene name
        """
        self.scene_name:str = value
        return

    def set_current_scene_func(self, func:Callable) -> None:
        """
        sets current scene function.
        """
        self.current_scene_function = func
        return

    def current_scene(self) -> bool:
        """
        executes current scene's function.

        currently, scene returns bool, rather scene will be changed or not.  
        """
        return self.current_scene_function()

    def flush_signal_dict(self) -> None:
        """
        flushs signal dict... for somewhat reason? idk
        """
        self.signal_dict.clear()
        return

    def add_signal_list(self, new_signal:Signal) -> Signal:
        """
        adds new signal to scene's signal list....
        """
        self.signal_dict[new_signal.get_signal_name()] = new_signal
        return new_signal

    def add_signal_to_list_safely(self, new_signal:Signal) -> Signal:
        """
        makes signal name more uniquely, so avoiding hash collision.
        """
        new_name = new_signal.get_signal_name() + str(new_signal.get_signal_count())
        new_signal.set_signal_name(new_name)
        return self.add_signal_list(new_signal)

    def remove_signal_list(self, signal_name:str):
        """
        remove signal through name.
        """
        return self.signal_dict.pop(signal_name)

    def check_signal(self, signal_name: str):
        """
        checks weather signal of that name exists.
        """
        return signal_name in self.signal_dict

    def get_signal(self, signal_name:str) -> Signal:
        """
        returns signal.
        if there is no signal named like it, raises error
        """
        ret = self.signal_dict.get(signal_name)
        if ret is None:
            raise KeyError()
        return ret