"""
basic objects for being rendered.
positions are world-base.
"""

from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum
import pygame
from threeDbasic.objects.camera import Camera3D
from threeDbasic.rendering.render_componenet import RenderMode, TextureRendererComponent
from threeDbasic.math.vector import vector3
from threeDbasic.math.box import Box

class ShapeType(Enum):
    SPHERE = auto()
    BOX = auto()
    

class Object3d(ABC):
    def __init__(self, pos:vector3, faces:Faces, 
                 renderer:TextureRendererComponent, 
                 render_data: pygame.Color | pygame.Surface,
                 static:bool,
                 object_type:ShapeType,
                 radius:float = 0,
                 box:Box = Box()
                 ) -> None:
        self.faces:Faces = faces
        self.pos: vector3 = pos
        self.static:bool = static
        self.object_type:ShapeType = object_type
        if object_type == ShapeType.SPHERE:
            self.radius = radius
        elif object_type == ShapeType.BOX:
            self.size = box
        # Object having render componenet is quite abusrd.

    def object_bounding_box(self) -> Box:
        if self.object_type == ShapeType.BOX:
            return self.size.fix_center(self.pos)
        elif self.object_type == ShapeType.SPHERE:
            if self.radius < 0:
                raise ValueError("radius being 0")

            return Box(
                vector3(self.pos.x - self.radius, 
                        self.pos.y - self.radius, 
                        self.pos.z - self.radius),
                vector3(self.pos.x + self.radius, 
                        self.pos.y + self.radius, 
                        self.pos.z + self.radius)
            )
        else:
            raise NotImplementedError("unknown objectt type")

    def get_faces(self) -> list[Face]:
        return self.faces.faces