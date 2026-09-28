"""
world that has every objects in game.

"""
from threeDbasic.base.object import Object3d
from threeDbasic.base.optim.bvh import BVH
from threeDbasic.objects.camera import Camera3D
import pygame
from threeDbasic.base.faces import Face

class World3D():
    def __init__(self) -> None:
        self.objects: list[Object3d] = []
        self.bvh = BVH([])

    def add_obj(self, obj:Object3d):
        self.objects.append(obj)
        self.bvh.objects.append(obj)

    def setup(self):
        self.bvh.build_bvh()
        # it would take while, so not to call it that frequently.

    def render(self, camera:Camera3D, screen: pygame.Surface):
        self.painters_way(camera, screen) # for test!


    def painters_way(self, camera: Camera3D, screen: pygame.Surface):
        """
        draw objects by painter's method.
        for testing, so some laziness is approved.
        """
        self.objects.sort(key= lambda obj : (obj.pos - camera.pos).size_squared(), reverse=True)

        for obj in self.objects:
            # draw one object to another.
            faces = obj.faces
            polygon: list[tuple[float, float]] = []
            for face in faces:
                if not camera.camera_visible_surface(face):
                    continue
                polygon = camera.total_pos_changing(face, 800, 600)

                pygame.draw.polygon(screen, face.color, polygon)
