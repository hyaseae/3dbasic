"""
a canvas that includes every ui objects and on.
"""

from UI.ui_base import UIBasic 
from threeDbasic.math.vector import vector3

class canvas(UIBasic):
    def __init__(self, width:int = 800, height:int = 600, pos: vector3 = vector3(0,0,0)) -> None:
        self.items:list[UIBasic] = []
        self.width: int = width
        self.height: int = height
        self.items_sorted : bool = True
        super().__init__(pos, 0)

    def render(self):
        """
        renders the whole canvas and its items.
        """
        if not super().get_visibility():
            return
        if not self.items_sorted:
            self.items.sort()
        for item in self.items:
            item.render()

    def add_item(self, new_item:UIBasic):
        """
        adds certain object to render line.
        """
        self.items.append(new_item)
        self.items_sorted = False
    
