"""
a canvas that includes every ui objects and on.
"""

from UI.ui_base import UIBasic 
from threeDbasic.math.vector import vector3
from pygame import Surface
from gamebasic.objects.UI.button import Button
from pygame.event import Event
import pygame

class canvas(UIBasic):
    def __init__(self, width:int = 800, height:int = 600, pos: vector3 = vector3(0,0,0)) -> None:

        self.items:list[UIBasic] = []
        self.width: int = width
        self.height: int = height
        self.items_sorted : bool = True
        
        super().__init__(pos, 0)

    def render(self, screen:Surface):
        """
        renders the whole canvas and its items.
        """
        if not super().get_visibility():
            return
        if not self.items_sorted:
            self.items.sort()
            self.items_sorted = True
        for item in self.items:
            if item.get_visibility():
                item.render(screen)

    def add_item(self, new_item:UIBasic):
        """
        adds certain object to render line.
        """
        self.items.append(new_item)
        self.items_sorted = False

    def check_event(self, event):
        self.check_buttons(event=event)
        # maybe added later
    
    def check_buttons(self, event:Event):
        for item in self.items:
            if isinstance(item, Button) and item.get_visibility():
                # for buttons, we only need to check click events.
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if item.is_mouse_in_button(event.pos):
                        item.clicked()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    item.released()