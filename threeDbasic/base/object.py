"""
basic objects for being rendered.
positions are world-base.
"""

from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum
import pygame
from threeDbasic.objects.camera import Camera3D
from threeDbasic.rendering.render_componenet import RenderMode, RendererComponent

class Object3d(ABC):
    def __init__(self, faces:Faces, renderer:RendererComponent, render_data: pygame.Color | pygame.Surface) -> None:
        self.faces:Faces = faces
        self.renderer:RendererComponent = renderer
        self.render_data = render_data

    def render(self, screen:pygame.Surface, camera:Camera3D):
        """
        renders itself at given screen, with perspective of camera.
        """
        self.renderer.render(screen, camera, self.render_data)
