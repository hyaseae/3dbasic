from threeDbasic.math.vector import vector3,ZERO
from threeDbasic.math.ray import Ray



class Box():
    def __init__(self, p1:vector3 = ZERO, p2:vector3 = ZERO) -> None:
        self.small_pos = vector3(min(p1.x,p2.x),min(p1.y,p2.y),min(p1.z,p2.z))
        self.big_pos = vector3(max(p1.x,p2.x),max(p1.y,p2.y),max(p1.z,p2.z))

    def point_in_box(self, point:vector3) -> bool:
        if (self.small_pos.x <= point.x <= self.big_pos.x and
            self.small_pos.y <= point.y <= self.big_pos.y and
            self.small_pos.z <= point.z <= self.big_pos.z):
            return True
        return False

    def ray_intersect_with_box(self, ray:Ray) -> bool:
        near = 0
        far = float("inf")
        for axis in range(3):
            origin = ray.pos[axis]
            direction = ray.direction[axis]
            lower, upper = self.small_pos[axis], self.big_pos[axis]

            if direction == 0:
                if origin < lower or origin > upper:
                    return False
                continue

            first = (lower - origin) / direction
            second = (upper - origin) / direction
            near = max(near, min(first, second))
            far = min(far, max(first, second))
            if near > far:
                return False
        return True

    def fix_center(self, pos:vector3):
        new_big_pos = pos + (self.big_pos - self.small_pos) / 2
        new_small_pos = pos - (self.big_pos - self.small_pos) / 2
        return Box(new_small_pos, new_big_pos)


def combined_box(box1:Box, box2:Box) -> Box:
    return Box(
        vector3(min(box1.small_pos.x, box2.small_pos.x),
                min(box1.small_pos.y, box2.small_pos.y),
                min(box1.small_pos.z, box2.small_pos.z)
                ),
        vector3(max(box1.big_pos.x, box2.big_pos.x),
                max(box1.big_pos.y, box2.big_pos.y),
                max(box1.big_pos.z, box2.big_pos.z)
                )
    )

def combined_boxes(boxes:list[Box]) -> Box:
    smallest_pos:vector3 = boxes[0].small_pos
    biggest_pos:vector3 = boxes[0].big_pos

    for box in boxes:
        for i in range(3):
            if smallest_pos[i] > box.small_pos[i]:
                smallest_pos[i] = box.small_pos[i]
            if biggest_pos[i] < box.big_pos[i]:
                biggest_pos[i] = box.big_pos[i]
    return Box(smallest_pos,biggest_pos)

