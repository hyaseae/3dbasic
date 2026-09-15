"""
img on ui. note that ui is static.
"""

from UI.ui_base import UIBasic
from threeDbasic.math.vector import vector3
from pygame import Surface
import pygame

class Img(UIBasic):
    def __init__(self, img:Surface, pos: vector3 = vector3(0, 0, 0), render_order: int = 0) -> None:
        
        self.img: Surface = img
        super().__init__(pos, render_order)

    def change_img(self, new_img:Surface):
        """
        changes image.
        """
        self.img:Surface = new_img

    def change_size(self, sizex:int, sizey:int):
        """
        change img's size with pygame.transform. note that it is lossy function.
        """
        self.img = pygame.transform.scale(self.img, (sizex, sizey))

    def render(self, screen:pygame.Surface):
        """
        renders it's img.
        note that this works as bliting to the background.
        """
        screen.blit(self.img, self.get_pos().to_2d_tuple())

def load_img(file_location:str = "", transparant:bool = False) -> Surface:
    """
    loads file and returns Surface object.
    """
    if transparant:
        return pygame.image.load(filename=file_location).convert_alpha()
    return pygame.image.load(filename=file_location).convert()
    