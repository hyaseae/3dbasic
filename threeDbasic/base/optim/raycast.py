from threeDbasic.math.ray import Ray
from threeDbasic.math.vector import vector3
from threeDbasic.base.optim.bvh import BVH, BVHNode
from threeDbasic.base.object import Object3d
from threeDbasic.base.faces import Face, Faces
from threeDbasic.base.constants import INF
from threeDbasic.math.vector import dot, is_similar_vector, cross
from threeDbasic.math.calc import is_similar


class Raycast(Ray):
    """
    a ray object tipically made for ray casting.
    """
    def __init__(self, pos: vector3, direction: vector3) -> None:
        super().__init__(pos, direction)

    def cast(self, bvh_tree: BVH) -> tuple[float, Face | None]:
        """
        returns first Face that touches ray.
        """

        plausible_objects = bvh_tree.get_plausible_objects(self)

        closest_face = None
        closest_t = INF

        for obj in plausible_objects:
            t, face = self.intersection_distance_with_obj(obj)
            if t < closest_t:
                closest_face = face
                closest_t = t

        return closest_t, closest_face

        # checks all objects that really touches ray.

        # sort them with distance.

        # returns.

    def intersection_distance_with_obj(self, obj:Object3d) -> tuple[float, Face | None]:
        t = INF
        closest_face:Face = obj.get_faces()[0]
        for face in obj.get_faces():
            t_ = self.intersection_distance_with_face(face)
            if t > t_:
                closest_face = face
                t = t_

        return t, closest_face

    def intersection_distance_with_face(self, face:Face) -> float:
        if len(face.points) <= 2:
            raise ValueError("face does not have sufficient points!")

        p0, p1, p2 = face.points[:3]
        edge1 = p1 - p0
        edge2 = p2 - p0

        h = cross(self.direction, edge2)
        determinant = dot(edge1, h)

        if is_similar(determinant, 0):
            return INF

        inverse = 1.0 / determinant
        offset = self.pos - p0
        u = inverse * dot(offset, h)
        if u < 0 or u > 1:
            return INF

        q = cross(offset, edge1)
        v = inverse * dot(self.direction, q)
        if (v < 0 or u + v > 1):
            return INF

        t = inverse * dot(edge2, q)
        return t if t >= 0 else INF
