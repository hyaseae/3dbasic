"""
simple button
"""

from pygame import Surface
from gamebasic.objects.UI.img import Img
from threeDbasic.math.vector import vector3
from gamebasic.debug.err_img import ERR_IMG
from gamebasic.debug.err_func import err_func
from typing import Callable
import pygame

class Button(Img):
    def __init__(self, img: Surface = ERR_IMG, clicked_img:Surface = ERR_IMG, pos: vector3 = vector3(0, 0, 0), render_order: int = 0, width:int = 0, height:int = 0, onclick:Callable = err_func, onclick_argument :object | None =None) -> None:
        super().__init__(img, pos, render_order)
        self.non_click_img:Surface = img
        self.clicked_img : Surface = clicked_img
        self.width = width
        self.height = height
        self.onclick:Callable = onclick
        self.onclick_argument = onclick_argument

        self.rect = pygame.Rect(int(pos.x), int(pos.y), width, height)
        self.change_size(self.width,self.height)

    def change_pos(self, new_pos: vector3):
        super().change_pos(new_pos)
        self.rect.topleft = (int(new_pos.x), int(new_pos.y))

    # render function follows img(super)'s behavior.

    def change_size(self, sizex: int, sizey: int) -> None:
        """
        changes size of a button.
        """
        self.width, self.height = sizex, sizey
        self.rect.size = (sizex, sizey)
        super().change_size(sizex, sizey)

    def is_mouse_in_button(self, mousepos:tuple[int,int])->bool:
        """
        check a given coordinates is in button's range.
        """
        # Keep hit testing in sync when the position vector was changed directly.
        self.rect.topleft = (int(self.pos.x), int(self.pos.y))
        return self.rect.collidepoint(mousepos)
    
    def clicked(self):
        self.img = self.clicked_img
        if self.onclick_argument is None:
            self.onclick()
        else:
            self.onclick(self.onclick_argument)

    def released(self):
        self.img = self.non_click_img