
from abc import ABC, abstractmethod
from threeDbasic.math.vector import vector3
from enum import Enum, auto
from threeDbasic.math.ray import Ray

class LightType(Enum):
    DIRECTIONAL = auto() # light as sun
    SPHERICAL = auto()
    LAZER = auto()


class Light(ABC):
    def __init__(self, pos:vector3) -> None:
        self.pos = pos
        self.color = (255,255,255) # bascially white.

class DirectionalLight(Light):
    def __init__(self, pos: vector3, direction:vector3) -> None:
        super().__init__(pos)
        self.direction = direction

class SphericalLight(Light):
    def __init__(self, pos: vector3) -> None:
        super().__init__(pos)

class LazerLight(Light):
    def __init__(self, pos: vector3, direction:vector3) -> None:
        self.ray = Ray(pos, direction)
        self.pos = pos