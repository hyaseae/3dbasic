from threeDbasic.math.vector import vector3, e1, e2, e3, cross, dot
from threeDbasic.math.calc import is_similar

class plane3D():
    """
    3d plane. including points and normals.
    """
    def __init__(self, point:vector3 = vector3(0, 0, 0), normal: vector3 = e3, vector_a: vector3 = e1) -> None:
        """
        point: one vector define plane's location
        normal: plane's normal vector.
        vector_a, vector_b(selective) : perpendicular vectors in plane.
        """
        self.fix(point, normal, vector_a)

    def is_point_in_plane(self, point:vector3) -> bool:
        """
        decides rather vector is in plane or not.
        """
        return is_similar(dot(point - self.point, self.normal), 0)

    def intersection_with_line(self, point: vector3, direction: vector3) -> vector3:
        """
        through a give direction, calculates a intersection point.

        this is technically a linear algebratic calculation, so using numpy can enhance performance.

        """

        # check if normal and direction is parallel
        if is_similar(dot(self.normal, direction), 0):
            # they are parallel, so there is no interseciton in reasonable amount of space.
            return point

        t = dot((self.point - point), self.normal) / dot(direction, self.normal)
        return point + (t * direction)

    def orthographic_projection_point(self, point:vector3):
        """
        returns a give vector's orthographic projection point.
        """
        return self.intersection_with_line(point, -1 * self.normal)

    def get_basis(self) -> tuple[vector3, vector3, vector3]:
        """
        returns plane's two perpendicular vectors and normals, in order.
        """
        return self.vector_a, self.vector_b, self.normal

    def fix(self, pos:vector3, normal:vector3, vector_a:vector3) -> None:
        """
        sets default arguments without memory leak i guess?
        """
        self.point: vector3 = pos
        self.normal: vector3 = normal.normalize()
        self.vector_a: vector3 = vector_a.normalize() if is_similar(dot(vector_a, self.normal), 0) else cross(normal, normal + e1).normalize()

        #vector a, b: perpendicular vectors exists in plane.
        self.vector_b: vector3 = cross(self.normal, self.vector_a)


def basis_transform(point:vector3, x:vector3 = e1, y:vector3 = e2, z:vector3 = e3) -> vector3:
    """
    transforms a given xyz basis vector to other basis's vectors. 
    I'm not certain that this works...?
    """
    return vector3(dot(x, point), dot(y, point), dot(z, point))