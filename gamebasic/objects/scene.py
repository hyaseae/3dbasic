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
        self.log = LOG()

    def tick(self, screen) -> bool:
        """
        updates and renders scene.
        """
        changed:bool = self.update()
        self.render(screen)
        return changed

    def update(self) -> bool:
        """
        handle events, check scene changes and more.
        """
        raise NotImplementedError()
        

    def render(self, screen):
        """
        renders the scene.
        """
        pass