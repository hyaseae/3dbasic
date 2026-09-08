from threeDbasic.math.vector import vector3, dot, cross
import pygame

class face():
    def __init__(self, p_initialized = False, points:list[vector3] = [], color = pygame.Color(255,255,255)) -> None:
        if (p_initialized):
            self.points:list[vector3] = points
        else:
            self.points:list[vector3] = []

        self.color = color
        

    def add_point(self, point:vector3):
        self.points.append(point)

    def normal_vector(self) -> vector3:
        """returns normal vector of face. """
        return cross(self.points[0] - self.points[1], self.points[0] - self.points[2])

    def average_point(self) -> vector3:
        sum_ = vector3(0,0,0)
        for v in self.points:
            sum_ += v
        return sum_ / len(self.points)


    def is_point_on_face(self, pos:vector3) -> tuple[bool, float]:
        """
        confirms if point can led a right angled line to face.
        """
        lengths = []
        for v in self.points:
            lengths.append((v-pos).size_squared)

        normal = self.normal_vector()
        d = -1 * dot(normal, self.points[0])
        dist = (dot(normal, pos) + d) ** 2 / normal.size_squared()
        lengths.append(dist)

        smallest = min(lengths)
        if smallest >= dist - 1e-10:
            return (True, smallest)
        return (False, smallest)

    def real_dist_long_squared(self, pos:vector3) -> float:
        """
        get real distance from position.
        """
        _, dist = self.is_point_on_face(pos)
        return dist

    def get_points(self) -> list[vector3]:
        """
        return face's points list.
        """
        return self.points

def trianglize(surface:face) -> list[face]:
    ret = []
    for i in range(len(surface.points) - 2):
        ret.append(face(True, [surface.points[0], surface.points[i+1], surface.points[i+2]]))
    return ret



class faces():
    def __init__(self):
        self.faces:list[face] = []

    def add_face(self, new_face:face) -> None:
        self.faces.append(new_face)

    def add_faces(self, new_face_list:list[face]) -> None:
        self.faces.extend(new_face_list)

    def __getitem__(self, key):
        self.faces.__getitem__(key)

