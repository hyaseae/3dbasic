from gamebasic.math.vector import vector3
from enum import Enum, auto

class CameraProjectionMode(Enum):
    ORTHOGRAPHIC = auto()
    PERSPECTIVE = auto()

class Camera2D():
    """
    a class for 2d camera.
    """
    def __init__(self) -> None:
        self.pos = vector3(0, 0, 100)
        self.normal = vector3(0, 0, -1)
        