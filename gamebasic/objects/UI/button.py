"""
simple button
"""

from pygame import Surface

from UI.img import Img
from threeDbasic.math.vector import vector3

class Button(Img):
    def __init__(self, img: Surface, clicked_img:Surface, pos: vector3 = vector3(0, 0, 0), render_order: int = 0, width:int = 0, height:int = 0) -> None:
        super().__init__(img, pos, render_order)
        self.non_click_img:Surface = img
        self.clicked_img : Surface = clicked_img
        self.width = width
        self.height = height
        self.change_size(self.width,self.height)

    def render(self, screen: Surface):
        return super().render(screen)

    def change_size(self, sizex: int, sizey: int) -> None:
        """
        changes size of a button.
        """
        self.width, self.height = sizex, sizey
        super().change_size(sizex, sizey)

    def is_mouse_in_button(self, mousepos:tuple[int,int])->bool:
        """
        check a given coordinates is in button's range.
        """
        return (self.pos.x - self.width/2 <= mousepos[0] <= self.pos.x + self.width/2) \
            and (self.pos.y - self.height/2 <= mousepos[1] <= self.pos.y + self.height/2)
    
    def clicked(self):
        self.img = self.clicked_img

    def released(self):
        self.img = self.non_click_img