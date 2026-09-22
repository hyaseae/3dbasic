"""
a class for putting texture in face.
"""
import pygame
from pygame import Surface
from threeDbasic.debug.err_img import ERR_IMG
from os.path import join as jr


class Texture():
    def __init__(self) -> None:

        self.failed_img = load_cached_texture(jr("threeDbasic", "debug", "missing_img.jpg"))
        

        pass


def load_texture(file_location:str = "", failed_img = ERR_IMG) -> Surface:
    """
    loads file and returns Surface object.
    """
    try:
        image = pygame.image.load(file_location)
        if pygame.display.get_surface() is None:
            return image
        return image.convert()
    except (OSError, pygame.error):
        return failed_img

_IMAGE_CACHE: dict[str, pygame.Surface] = {}
def load_cached_texture(path:str) -> pygame.Surface:
    if path not in _IMAGE_CACHE:
        _IMAGE_CACHE[path] = load_texture(path)
    return _IMAGE_CACHE[path]