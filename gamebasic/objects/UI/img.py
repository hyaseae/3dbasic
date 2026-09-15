"""
img on ui
"""

from UI.ui_base import UIBasic
from threeDbasic.math.vector import vector3

class Img(UIBasic):
    def __init__(self, img, pos: vector3 = vector3(0, 0, 0), render_order: int = 0) -> None:
        

        super().__init__(pos, render_order)