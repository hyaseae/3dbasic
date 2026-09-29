

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
    OBJ_COLOR = auto() # fill face colors that object already have.
    LIGHTED_OBJ_COLOR = auto()

class TextureRendererComponent(ABC):
    """
    component for rendering.
    this thing only gives texture, so other rendering should be done in renderer.
    """
    def __init__(self, render_mode:RenderMode, render_data: pygame.Surface | pygame.Color) -> None:
        self.render_mode: RenderMode = render_mode
        self.render_data = render_data

    @abstractmethod
    def render(self, screen:pygame.Surface, camera:Camera3D, faces:Faces) -> None:
        raise NotImplementedError()

    @abstractmethod
    def apply_light(self):
        raise NotImplementedError()

class ColorRenderer(TextureRendererComponent):
    def __init__(self, color:pygame.Color, render_mode: RenderMode) -> None:
        super().__init__(render_mode, color)
        if self.render_mode == RenderMode.LIGHTED_COLOR or self.render_mode == RenderMode.LIGHTED_OBJ_COLOR:
            self.using_light = True
        elif self.render_mode == RenderMode.SIMPLE_COLOR or self.render_mode == RenderMode.OBJ_COLOR:
            self.using_light = False
        else:
            raise TypeError("Rendermode is not correct!")
        
    def render(self, screen: pygame.Surface, camera: Camera3D, faces:Faces):

        if self.render_mode == RenderMode.LIGHTED_COLOR:
            self.apply_light # currently, not Implemented.

        if not isinstance(self.render_data, pygame.Color):
            raise TypeError("render data not matching with component type!")

        polygon: list[tuple[float, float]] = []
        for face in faces:
            if not camera.camera_visible_surface(face):
                continue
            polygon = camera.total_pos_changing(face, screen.get_width(), screen.get_height())

            if self.render_mode == RenderMode.OBJ_COLOR:
                pygame.draw.polygon(screen, face.color, polygon)
            else:
                pygame.draw.polygon(screen, self.render_data, polygon)


    def apply_light(self):
        pass

class ImageRenderer(TextureRendererComponent):
    def __init__(self, color:pygame.Color, render_mode: RenderMode, render_data: pygame.Surface | pygame.Color) -> None:
        super().__init__(render_mode, render_data)
        self.color = color
        if self.render_mode == RenderMode.LIGHTED_COLOR:
            self.using_light = True
        elif self.render_mode == RenderMode.SIMPLE_COLOR:
            self.using_light = False
        else:
            raise TypeError("Rendermode is not correct!")

    def render(self, screen: Surface, camera: Camera3D, faces:Faces):
        pass # TODO

    def apply_light(self):
        pass


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