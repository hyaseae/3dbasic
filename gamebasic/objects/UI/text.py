"""
text on ui. note that ui is static.
"""

from gamebasic.objects.UI.ui_base import UIBasic
from threeDbasic.math.vector import vector3
from pygame import Surface
import pygame
from gamebasic.debug.err_img import ERR_IMG
from gamebasic.objects.UI.img import Img

class Text(Img):
    def __init__(self, text:str = "", background_img:Surface = ERR_IMG, pos: vector3 = vector3(0, 0, 0), 
                 render_order: int = 0, 
                 font_name: str = "", 
                 color:pygame.Color = pygame.Color(0,0,0)) -> None:
        self.text: str = text
        self.text_surface: Surface = background_img
        self.font_name: str = font_name
        self.color: pygame.Color = color

        self.font:pygame.font.Font = load_cached_font(self.font_name)
        self.make_text(text, self.font, self.color)
        super().__init__(background_img, pos, render_order)

    def change_text(self, new_text:str):
        self.text = new_text
        self.refresh()

    def change_color(self, new_color:pygame.Color):
        self.color = new_color
        self.refresh()

    def refresh(self):
        """
        remakes text again.
        """
        self.text_surface = self.img # refreshes background.
        self.font = load_cached_font(self.font_name)
        self.make_text(self.text, self.font, self.color)

    def make_text(self, new_text:str,
                  font: pygame.font.Font,
                  color:pygame.Color = pygame.Color(0,0,0), 
                  anti_aliasing:bool = True) -> None:
        """
        make text 
        """
        self.text_surface = font.render(new_text, anti_aliasing, color)

    def change_size(self, sizex:int, sizey:int):
        """
        change img's size with pygame.transform. note that it is lossy function.
        """
        self.text_surface = pygame.transform.scale(self.text_surface, (sizex, sizey))

    def render(self, screen:pygame.Surface):
        """
        renders it's text.
        note that this works as bliting to the background.
        """
        screen.blit(self.text_surface, self.get_pos().to_2d_tuple())

def load_font(file_location:str = "", font_size:int = 36, failed_img:Surface = ERR_IMG) -> pygame.font.Font:
    """
    loads file and returns Surface object.
    """
    try:
        font = pygame.font.Font(file_location,size=font_size)
        return font
    except (OSError, pygame.error):
        return pygame.font.SysFont("Arial", font_size)

_FONT_CACHE: dict[str, pygame.font.Font] = {}
def load_cached_font(path:str) -> pygame.font.Font:
    if path not in _FONT_CACHE:
        _FONT_CACHE[path] = load_font(path)
    return _FONT_CACHE[path]