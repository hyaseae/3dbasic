"""
basic ui component.
note that positions are pygame-style.
"""

from abc import ABC, abstractmethod
from threeDbasic.math.vector import vector3


class UIBasic():

    def __init__(self, pos:vector3 = vector3(0, 0, 0), render_order : int = 0) -> None:
        self.visible: bool = True
        self.pos: vector3 = pos
        self.render_order = render_order

    def make_visible(self):
        """
        makes a ui object visible.
        """
        self.visible = True

    def make_invisible(self):
        """
        makes a ui object invisible.
        """
        self.visible = False

    def get_render_order(self) -> int:
        """
        returns this object's render order.
        """
        return self.render_order

    def get_visibility(self) -> bool:
        """
        returns this object's visibility
        """
        return self.visible

    def __lt__(self, other):
        if isinstance(other, UIBasic):
            return self.render_order < other.render_order
        else:
            raise TypeError("ui object can be only compared to ui objects!")

    def __gt__(self, other):
        if isinstance(other, UIBasic):
            return self.render_order > other.render_order
        else:
            raise TypeError("ui object can be only compared to ui objects!")

    def __le__(self, other):
        if isinstance(other, UIBasic):
            return self.render_order <= other.render_order
        else:
            raise TypeError("ui object can be only compared to ui objects!")

    def __ge__(self, other):
        if isinstance(other, UIBasic):
            return self.render_order >= other.render_order
        else:
            raise TypeError("ui object can be only compared to ui objects!")

    def __eq__(self, value: object) -> bool:
        return not (self > object or self < object)

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(object)
    

    @abstractmethod
    def render(self):
        """
        renders itself.
        """
        pass

