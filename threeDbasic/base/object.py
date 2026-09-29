"""
basic objects for being rendered.
positions are world-base.
"""

from threeDbasic.base.faces import Face,Faces
from abc import abstractmethod, ABC
from enum import auto, Enum
from math import isfinite
import pygame
from threeDbasic.objects.camera import Camera3D
from threeDbasic.rendering.render_componenet import RenderMode, TextureRendererComponent
from threeDbasic.math.vector import vector3
from threeDbasic.math.box import Box

class ShapeType(Enum):
    SPHERE = auto()
    BOX = auto()
    

class Object3d(ABC):
    def __init__(self, faces:Faces, 
                 renderer:TextureRendererComponent, 
                 static:bool = False,
                 object_type:ShapeType = ShapeType.SPHERE,
                 pos:vector3 = vector3(0, 0, 0), 
                 radius:float = 0,
                 box:Box = Box(),
                 scale: float = 1
                 ) -> None:
        self.faces:Faces = faces
        self.pos: vector3 = pos
        self.static:bool = static
        self.object_type:ShapeType = object_type
        self.renderer:TextureRendererComponent = renderer

        if object_type == ShapeType.SPHERE:
            self.radius = radius
        elif object_type == ShapeType.BOX:
            self.size = box
        # Object having render componenet is quite abusrd.

        self.fix_face_points()
        if scale != 1:
            self.scale(scale)

    def fix_face_points(self):
        translated_points: dict[int, vector3] = {}
        for face in self.faces:
            for index, point in enumerate(face.get_points()):
                translated_point = translated_points.get(id(point))
                if translated_point is None:
                    translated_point = point + self.pos
                    translated_points[id(point)] = translated_point
                face.points[index] = translated_point

    def scale(self, factor: float) -> None:
        """Scale the object's vertices uniformly around its position."""
        if not isfinite(factor) or factor < 0:
            raise ValueError("scale factor must be finite and non-negative")

        scaled_points: dict[int, vector3] = {}
        for face in self.faces:
            for index, point in enumerate(face.get_points()):
                scaled_point = scaled_points.get(id(point))
                if scaled_point is None:
                    scaled_point = self.pos + (point - self.pos) * factor
                    scaled_points[id(point)] = scaled_point
                face.points[index] = scaled_point

        if self.object_type == ShapeType.SPHERE:
            self.radius *= factor
        elif self.object_type == ShapeType.BOX:
            half_size = (self.size.big_pos - self.size.small_pos) * (factor / 2)
            self.size = Box(-1 * half_size, half_size)


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
            raise NotImplementedError("unknown object type")

    def get_faces(self) -> list[Face]:
        return self.faces.faces

    def render(self, camera:Camera3D, screen:pygame.Surface):
        self.renderer.render(screen=screen, camera=camera, faces=self.faces)