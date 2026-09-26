

from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum
import pygame
from threeDbasic.objects.camera import Camera3D
from pygame import Surface
from threeDbasic.debug.err_img import ERR_IMG
from os.path import join as jr

class RenderMode(Enum):
    SIMPLE_COLOR = auto() # fill all face with simple color. does not apply light, so fast. 
    SIMPLE_IMG = auto() # fill all faces with simple img. does not apply transforming or lighting.
    LIGHTED_IMG = auto() # fill faces with texture img, apply lightings.
    LIGHTED_COLOR = auto() # fill faces colors, and apply lightings.

class TextureRendererComponent(ABC):
    """
    component for rendering.
    this thing only gives texture, so other rendering should be done in renderer.
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

class ColorRenderer(TextureRendererComponent):
    def __init__(self, color:pygame.Color, faces: Faces, render_mode: RenderMode) -> None:
        super().__init__(faces, render_mode)
        self.color = color
        if self.render_mode == RenderMode.LIGHTED_COLOR:
            self.using_light = True
        elif self.render_mode == RenderMode.SIMPLE_COLOR:
            self.using_light = False
        else:
            raise TypeError("Rendermode is not correct!")
        
    def render(self, screen: pygame.Surface, camera: Camera3D, render_data: pygame.Surface | pygame.Color):
        
        pass

class ImageRenderer(TextureRendererComponent):
    def __init__(self, color:pygame.Color, faces: Faces, render_mode: RenderMode) -> None:
        super().__init__(faces, render_mode)
        self.color = color
        if self.render_mode == RenderMode.LIGHTED_COLOR:
            self.using_light = True
        elif self.render_mode == RenderMode.SIMPLE_COLOR:
            self.using_light = False
        else:
            raise TypeError("Rendermode is not correct!")


class Texture():
    def __init__(self) -> None:

        self.failed_img = load_cached_texture(jr("threeDbasic", "debug", "missing_img.jpg"))
        

        pass


def load_texture(file_location:str = "", failed_img = ERR_IMG) -> Surface:
    """
    loads file and returns Surface object.
    """
    try:
        image = pygame.image.load(file_location)
        if pygame.display.get_surface() is None:
            return image
        return image.convert()
    except (OSError, pygame.error):
        return failed_img

_IMAGE_CACHE: dict[str, pygame.Surface] = {}
def load_cached_texture(path:str) -> pygame.Surface:
    if path not in _IMAGE_CACHE:
        _IMAGE_CACHE[path] = load_texture(path)
    return _IMAGE_CACHE[path]