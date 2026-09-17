"""
total signals for global data transforming

"""
from gamebasic.debug.logging import LOG


def err_func():
    """ function for err"""
    raise FileNotFoundError()

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
        raise NotImplementedError()