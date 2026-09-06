from threeDbasic.math.vector import vector3, e1, e2, e3, cross, dot
from threeDbasic.base.constants import EPSILONE

class plane3D():
    def __init__(self, point:vector3 = vector3(0, 0, 0), normal: vector3 = e3, vector_a: vector3 = e1) -> None:
        """
        point: one vector define plane's location
        normal: plane's normal vector.
        vector_a, vector_b(selective) : perpendicular vectors in plane.
        """
        self.point: vector3 = point
        self.normal: vector3 = normal.normalize()
        self.vector_a: vector3 = vector_a.normalize() if abs(dot(normal, vector_a)) <= EPSILONE else cross(normal, normal + e1).normalize()

        #vector a, b: perpendicular vectors exists in plane.
        self.vector_b: vector3 = cross(self.normal, self.vector_a)

    def point_in_plane(self, point:vector3) -> bool:
        """
        decides rather vector is in plane or not.
        """
        return dot(point - self.point, self.normal) <= EPSILONE

    def intersection_with_line(self, point: vector3, direction: vector3) -> vector3:
        """
        through a give direction, calculates a intersection point.

        this is technically a linear algebratic calculation, so using numpy can enhance performance.

        """

        # check if normal and direction is parallel
        if abs(dot(self.normal, direction)) <= EPSILONE:
            # they are parallel, so there is no interseciton in reasonable amount of space.
            return point

        

        return point