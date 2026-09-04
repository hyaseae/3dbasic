from enum import Enum, auto

from gamebasic.objects.signal import Signal

class SceneName(Enum):
    """
    enum class for scenes' name
    """
    NONE = auto()
    HOME = auto()



class Scene():
    """
    scene class that gets global datas.
    maybe used in save things?
    """
    def __init__(self) -> None:
        self.scene_name = SceneName.NONE
        def err_func():
            raise FileNotFoundError()
        self.current_scene_function = err_func
        self.signal_dict:dict[str, Signal] = {}

    def get_current_scene_enum(self)-> SceneName:
        """
        returns current scene name(enum)
        """
        return self.scene_name

    def set_current_scene_enum(self, value) -> None:
        """
        sets current scene name
        """
        self.scene_name = value
        return

    def current_scene(self) -> None:
        """
        executes current scene's function. 
        """
        return self.current_scene_function()

    def flush_signal_dict(self) -> None:
        """
        flushs signal dict... for somewhat reason? idk
        """
        self.signal_dict.clear()
        return

    def add_signal_list(self, new_signal:Signal):
        """
        adds new signal to scene's signal list....
        """
        self.signal_dict[new_signal.get_signal_name()] = new_signal
        return

    def remove_signal_list(self, signal_name:str):
        """
        remove signal through name.
        """
        return self.signal_dict.pop(signal_name)
