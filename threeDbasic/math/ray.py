from threeDbasic.math.vector import vector3



class Ray():
    def __init__(self, pos:vector3, direction:vector3) -> None:
        self.pos:vector3 = pos
        self.direction:vector3 = direction