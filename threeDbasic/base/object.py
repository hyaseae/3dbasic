"""
basic objects for being rendered.
positions are world-base.
"""

from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum

class RenderMode(Enum):
    SIMPLE_COLOR = auto()
    SIMPLE_IMG = auto()
    TEXTURE = auto()


class Object3d(ABC):
    def __init__(self, faces:Faces, render_mode: RenderMode) -> None:
        self.faces:Faces = faces
        self.render_mode: RenderMode = render_mode
        
