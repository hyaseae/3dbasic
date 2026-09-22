



from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum
import pygame
from threeDbasic.objects.camera import Camera3D

class RenderMode(Enum):
    SIMPLE_COLOR = auto() # fill all face with simple color. does not apply light, so fast. 
    SIMPLE_IMG = auto() # fill all faces with simple img. does not apply transforming or lighting.
    TEXTURE = auto() # fill faces with texture img, apply lightings.
    LIGHTED_COLOR = auto() # fill faces colors, and apply lightings.

class RendererComponent(ABC):
    """
    component for rendering.
    """
    def __init__(self, faces:Faces, render_mode:RenderMode) -> None:
        self.faces:Faces = faces
        self.render_mode: RenderMode = render_mode

    @abstractmethod
    def render(self, screen:pygame.Surface, camera:Camera3D, render_data:pygame.Surface | pygame.Color):
        raise NotImplementedError()

    @abstractmethod
    def apply_light(self):
        raise NotImplementedError()

class ColorRenderer(RendererComponent):
    pass

class ImageRenderer(RendererComponent):
    pass