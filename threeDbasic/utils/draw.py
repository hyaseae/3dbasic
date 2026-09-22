import pygame
from threeDbasic.base.faces import Face, trianglize
from threeDbasic.objects.camera import Camera3D
from threeDbasic.math.plane import plane3D
from threeDbasic.math.vector import vector3



def render_face_orthographic(screen: pygame.Surface, camera: Camera3D, face:Face) -> None:
    """
    finally renders some face to the pygame surface, by given camera.
    """
    # if not visible, ignore it.
    if not (camera.camera_visible_surface_lazy(face)):
        return

    def unpack(point:vector3) -> list[float]:
        return [point.x, point.y]

    view_plane:plane3D = camera.get_view_plane()
    points_in_plane:list[list[float]] = []
    for point in face.get_points():
        points_in_plane.append(unpack(view_plane.orthographic_projection_point(point)))

    pygame.draw.polygon(screen, face.color, points_in_plane)

    return