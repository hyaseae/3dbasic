import pygame
from threeDbasic.math.vector import vector3, angle_diff, e3, rotation_throuh_axis, dot,ZERO
from threeDbasic.base.inrange import inrange
from threeDbasic.base.faces import Face, Faces
from threeDbasic.math.plane import plane3D
from threeDbasic.math.calc import is_similar
from math import pi, tan
from enum import Enum, auto
from threeDbasic.math.vector import is_similar_vector

class CameraProjectionMode(Enum):
    ORTHOGRAPHIC = auto()
    PERSPECTIVE = auto()

class Camera3D():
    """
    a camera object and utils.
    """
    def __init__(self, pos = vector3(0,0,0), horizontal_angle = pi/4, vertical_angle = pi/3, normal_vector = vector3(1,0,0), binomial_vector = vector3(0,0,1), initial_upside:vector3 = e3) -> None:
        """
        pos: absolute position of camera.
        horizontal_angle: a screen's width. if horizontal angle is 90 degrees, horizontally 45 degrees from normal veector will be shown.
        vertical_angle: a screen's height. if vertical angle is 60 degrees, vertically 30 degrees from normal veector will be shown.
        normal_vector: a vector that camera's screen center is directing. must be normal vector. x
        binomial_vector: a vector that camera's screen upside is directing. must be normal vector. z
        """
        self.pos:vector3 = pos
        self.horizontal_angle:float = horizontal_angle
        self.vertical_angle:float = vertical_angle
        self.normal_vector:vector3 = normal_vector.normalize()
        self.binomial_vector:vector3 = binomial_vector.normalize()
        self.initial_upside: vector3 = initial_upside
        self.mode:CameraProjectionMode = CameraProjectionMode.ORTHOGRAPHIC
        self.view_plane_dist:float = 1.0
        self.view_plane:plane3D = plane3D(self.pos + self.normal_vector * self.view_plane_dist, self.normal_vector, self.binomial_vector)

    def move_to_absloute_pos(self, x:float, y:float, z:float):
        """
        immediately change camera's position.
        """
        self.pos.change(x,y,z)

    # def look_at_certain_position(self, pos:vector3):
    #     """
    #     make self look at certain position, changing it's normal vector and binomial vector.
    #     position is not modified.
    #     """
    #     self.look_at_certain_direction(pos - self.pos)

    # def look_at_certain_direction(self, direction:vector3) -> None:
    #     """
    #     make self's normal vector look at certain direction.
    #     position is not modified.
    #     """
    #     if is_similar_vector(direction.normalize(), self.normal_vector):
    #         return
    #     side_vector = self.binomial_vector * self.normal_vector
    #     self.view_plane.fix(ZERO, self.normal_vector, self.binomial_vector)
    #     # make view plane positioned at origin for calculation.
    #     orthorized_direction = self.view_plane.orthographic_projection_point(direction)
    # NOTE: this freking thing is hard to make and currently useless, so just stop doign this. brrrrr

    
    def get_horizontal_balance(self):
        """
        returns how much amount screen has been rolled, returns only zero or positive values.
        
        NOT TESTED!!
        # TODO: TEST THIS.
        """
        cross_vector: vector3 = self.binomial_vector * self.normal_vector
        level_vector: vector3 = cross_vector.projection(vector3(cross_vector.x, cross_vector.y, 0).normalize())
        level_angle = angle_diff(cross_vector, level_vector, zeortopi=False)
        return level_angle

    def rotation_vertical(self, angle, limited = True, limited_angle = inrange(0.1, 1), clutching = False) -> None:
        """
        make a rotations on a normal vector and binomial vector.
        since hairy ball thm, binomial vector will define which direction is upward.
        limited controls upper(or below) overhead situation, true to be handled.
        clutching makes decision of rather rollback or revert the binomial vector's sign.

        NOT TESTED!!!
        # TODO: TEST THIS!
        """
        rot_axis:vector3 = (self.binomial_vector * self.normal_vector)
        rot_vector = rotation_throuh_axis(self.normal_vector, rot_axis, angle=angle)
        rot_binomial = (self.normal_vector * rot_axis)
        if not limited:
            self.normal_vector = rot_vector
            self.binomial_vector = rot_binomial
            return
        if not limited_angle.check_value(dot(self.initial_upside, rot_binomial)):
            if clutching:
                self.binomial_vector = rot_binomial * -1
                self.normal_vector = rot_vector
                return
            # do nothing.
            return

    def rotation_horizontal(self, angle, limited = True, limited_range = inrange(0, pi/10), barrelroll = False, e3rotation = False):
        """
        angle: amount of angle camera will be horizontally rotated. note that angle should be quite a small amount, so limited range's calculation fails more rarely.
        limited: if normal vector is already directing kinda upward or kinda downward, horizontal rotation might be end up with screen rotated with CW/CCW without intend. So, there are some options to provide alternative plans(e3rotation, barrelroll.) if limited is false, we just do rotation, no safe checks. recommended to be turned on.
        limited_range: range from 0 to some amount, allowed screen's roll amount. some accecptable amount of screen rolling is expected to enhance realistic.
        barrelroll: rather screen rolling will be allowed.
        e3rotation: rather not screen rolling will be allowed. if true, camera will be just rotated through e3 vector(z vector). precede than barrelroll.


        NOT TESTED!!!
        # TODO: TEST THIS!

        if barrelroll is false, it always do e3rotation.

        
        """
        if not limited:
            rot_vector = rotation_throuh_axis(self.normal_vector, self.binomial_vector, angle=angle)
            self.normal_vector = rot_vector
            return
        if e3rotation:
            rot_vector = rotation_throuh_axis(self.normal_vector, self.initial_upside, angle=angle)
            rot_binomial = rotation_throuh_axis(self.binomial_vector, self.initial_upside, angle=angle)
            self.normal_vector = rot_vector
            self.binomial_vector = rot_binomial
            return

        cross_vector: vector3 = self.normal_vector * self.binomial_vector
        level_vector: vector3 = cross_vector.projection(vector3(cross_vector.x, cross_vector.y, 0).normalize())
        if (not limited_range.check_value(angle_diff(cross_vector, level_vector, zeortopi=False)) or (not barrelroll)):
            self.rotation_horizontal(angle, e3rotation=True)
            return
        rot_vector = rotation_throuh_axis(self.normal_vector, self.binomial_vector, angle)
        self.normal_vector = rot_vector
        return


    def get_relative_pos_on_screen(self, absolute_vector: vector3, screen_width:int = 1600, screen_height:int = 900):
        """
        get an relative position of a outside vector.
        think screen's normal vector as (0, 0), and screen as cartesian coordinates.
        so, leftmost corner is (-W/2, H/2), it's angle is (-Horizontal angle/2, vertical angle/2) from normal vector, and rightmost corner is (W/2, -H/2), vice versa.
        
        to make it real screen pos, another function is needed.

        outside vector: is considered as a distance vector between a point and the camera, naturally non-zero vector.
        
        return values:
        relative_x, relative_y: float, float
        """
        if screen_width <= 0 or screen_height <= 0:
            raise ValueError("screen dimensions must be positive")
        if self.horizontal_angle <= 0 or self.horizontal_angle >= pi:
            raise ValueError("horizontal_angle must be between 0 and pi")
        if self.vertical_angle <= 0 or self.vertical_angle >= pi:
            raise ValueError("vertical_angle must be between 0 and pi")

        # The vector is already relative to the camera, as specified above.
        forward = self.normal_vector.normalize()
        up = self.binomial_vector.normalize()
        right = (forward * up).normalize()

        depth = dot(absolute_vector, forward)
        if depth <= 0:
            raise ValueError("absolute_vector must point in front of the camera")

        horizontal = dot(absolute_vector, right) / depth
        vertical = dot(absolute_vector, up) / depth
        half_horizontal = tan(self.horizontal_angle / 2)
        half_vertical = tan(self.vertical_angle / 2)

        return (
            screen_width / 2 * horizontal / half_horizontal,
            screen_height / 2 * vertical / half_vertical,
        )

    def camera_visible_surface_lazy(self, surface:Face, ignorance_range:inrange = inrange(0, 0.1), face_CCW= False) -> bool:
        """
        check if surface is visible from camera's view, roughly
        """
        normal = surface.normal_vector() if face_CCW else surface.normal_vector() * -1
        if dot(normal, self.normal_vector) <= 0:
            return False

        dist = surface.average_point() - self.pos
        # LAZY POINT
        if not ignorance_range.check_value(dist.size_squared()):
            # note that distance is squraed here.
            return False

        if dot(dist, self.normal_vector) <= 0:
            return False

        return True

    def camera_visible_surface(self, surface:Face, ignorance_range : inrange = inrange(0, 0.1), face_CCW = False) -> bool:
        """
        check if surface is visible.
        distance is checked more strictly, also note that this function is purposed on big faces.
        """

        normal = surface.normal_vector() if face_CCW else surface.normal_vector() * -1
        if dot(normal, self.normal_vector) <= 0:
            return False

        distance = surface.real_dist_long_squared(self.pos)
        if not ignorance_range.check_value(distance):
            # note that distance is squraed here.
            return False

        dist = surface.average_point() - self.pos
        if dot(dist, self.normal_vector) <= 0:
            return False

        return True

    def get_view_plane(self) -> plane3D:
        """
        returns self's view plane.
        """
        return self.view_plane

    def fix_view_plane(self) -> None:
        """
        fix self's view plane, since there might be some unsync issue.
        """
        self.view_plane.fix(self.pos + self.normal_vector * self.view_plane_dist, self.normal_vector, self.binomial_vector)


    def draw_everything_in_camera(self, face_objects: Faces):
        """
        given list of faces, and draw it manually.
        """



    