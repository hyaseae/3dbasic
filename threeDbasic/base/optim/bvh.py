from __future__ import annotations

from dataclasses import dataclass

from threeDbasic.base.object import Object3d
from threeDbasic.math.ray import Ray
from threeDbasic.math.box import Box, combined_boxes


_MAX_OBJECTS_PER_LEAF = 2


@dataclass
class BVHNode:
    # tree structure for bvh. 
    bounds: Box
    objects: list[Object3d] | None = None
    left: BVHNode | None = None
    right: BVHNode | None = None

class BVH():
    def __init__(self, objects:list[Object3d]) -> None:
        self.objects:list[Object3d] = objects
        self.root : BVHNode | None = None

    @classmethod
    def get_objects_bounding_box(cls, objects:list[Object3d]) -> Box:
        boxes = []
        for obj in objects:
            boxes.append(obj.object_bounding_box())
        return combined_boxes(boxes)

    @classmethod
    def build_node(cls, objects:list[Object3d]) -> BVHNode:
        bound = cls.get_objects_bounding_box(objects)
        if len(objects) <= _MAX_OBJECTS_PER_LEAF:
            # recursive ends.
            return BVHNode(bounds=bound, objects=objects)

        # split with boxes longest edge.
        longest_axis_to_split = max(
            range(3),
            key= lambda i: bound.big_pos[i] - bound.small_pos[i]
        )
        objects_sorted = sorted(objects, key=lambda obj: obj.pos[longest_axis_to_split])
        mid_index = len(objects_sorted) // 2
        return BVHNode(
            bounds=bound,
            left=cls.build_node(objects_sorted[:mid_index]),
            right=cls.build_node(objects_sorted[mid_index:])
        )
        
    def build_bvh(self) -> BVHNode | None:
        self.root = self.build_node(self.objects) if self.objects else None
        return self.root

    def get_plausible_objects(self, ray: Ray) -> list[Object3d]:
        """
        return objects from bvh tree.
        """
        if self.root is None:
            self.build_bvh()
        if self.root is None:
            return []

        plausible_objects: list[Object3d] = []
        nodes = [self.root]
        while nodes:
            node = nodes.pop()
            if not node.bounds.ray_intersect_with_box(ray):
                continue

            if node.objects is not None: # it means this node is leaf.
                plausible_objects.extend(node.objects)
            else:
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

        return plausible_objects
