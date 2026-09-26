from __future__ import annotations

from dataclasses import dataclass

from threeDbasic.base.object import Object3d, ObjectType
from threeDbasic.math.ray import Ray
from threeDbasic.math.box import Box, combined_boxes
from threeDbasic.math.vector import vector3

_MAX_OBJECTS_PER_LEAF = 2


@dataclass
class BVHNode:
    # LL for BVH
    bounds: Box
    objects: list[Object3d] | None = None
    left: BVHNode | None = None
    right: BVHNode | None = None

class BVH():
    def __init__(self, objects:list[Object3d]) -> None:
        self.objects:list[Object3d] = objects
        self.root : BVHNode | None = None

    def get_objects_bounding_box(self, objects:list[Object3d]):
        boxes = []
        for obj in objects:
            boxes.append(obj.object_bounding_box())
        return combined_boxes(boxes)

    def build_node(self, objects:list[Object3d]):
        bound = self.get_objects_bounding_box(objects)
        pass


    




# class BVHBox():
#     def __init__(self, objects:list[Object3d]) -> None:
#         self.objects = objects
#         self.root: _BVHNode | None = None
#     @classmethod
#     def _build_node(cls, objects: list[Object3d]) -> _BVHNode:
#         bounds = cls._combined_bounds(objects)
#         if len(objects) <= _MAX_OBJECTS_PER_LEAF:
#             return _BVHNode(bounds=bounds, objects=list(objects))

#         split_axis = max(
#             range(3),
#             key=lambda axis: bounds[1][axis] - bounds[0][axis],
#         )
#         sorted_objects = sorted(objects, key=lambda obj: obj.pos[split_axis])
#         midpoint = len(sorted_objects) // 2
#         return _BVHNode(
#             bounds=bounds,
#             left=cls._build_node(sorted_objects[:midpoint]),
#             right=cls._build_node(sorted_objects[midpoint:]),
#         )

#     def build_bvh(self) -> _BVHNode | None:
#         """
#         Build a BVH using each object's position and bounding-sphere radius.
#         """
#         self.root = self._build_node(self.objects) if self.objects else None
#         return self.root

#     @staticmethod
#     def _ray_intersects_bounds(ray: Ray, bounds: _Bounds) -> bool:
#         near = float("-inf")
#         far = float("inf")
#         for axis in range(3):
#             origin = ray.pos[axis]
#             direction = ray.direction[axis]
#             lower, upper = bounds[0][axis], bounds[1][axis]

#             if direction == 0:
#                 if origin < lower or origin > upper:
#                     return False
#                 continue

#             first = (lower - origin) / direction
#             second = (upper - origin) / direction
#             near = max(near, min(first, second))
#             far = min(far, max(first, second))
#             if near > far:
#                 return False

#         return far >= max(near, 0)

#     def get_plausible_objects(self, ray: Ray) -> list[Object3d]:
#         """
#         Return objects whose bounding boxes intersect the ray.
#         """
#         if self.root is None:
#             self.build_bvh()
#         if self.root is None:
#             return []

#         plausible_objects: list[Object3d] = []
#         nodes = [self.root]
#         while nodes:
#             node = nodes.pop()
#             if not self._ray_intersects_bounds(ray, node.bounds):
#                 continue

#             if node.objects is not None:
#                 plausible_objects.extend(node.objects)
#             else:
#                 if node.left is not None:
#                     nodes.append(node.left)
#                 if node.right is not None:
#                     nodes.append(node.right)

#         return plausible_objects
