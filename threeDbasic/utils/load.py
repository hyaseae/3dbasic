from threeDbasic.base.faces import Faces, Face
from threeDbasic.math.vector import vector3
import pygame

def read_off_file(location: str, globalty = False) -> Faces:
    """
    Read OFF vertices and faces, including optional per-face RGB or RGBA colors.
    Color channels in the range 0..1 are treated as normalized; larger channels
    are interpreted as 0..255 values.
    """
    model = Faces()
    with open(location, "r", encoding="UTF-8") as file:
        data_lines = (
            (line_number, content)
            for line_number, raw_line in enumerate(file, start=1)
            if (content := raw_line.partition("#")[0].strip())
        )

        def read_data_line() -> tuple[int, str]:
            try:
                return next(data_lines)
            except StopIteration as error:
                raise ValueError("Unexpected end of OFF file") from error

        line_number, header = read_data_line()
        header_fields = header.split()
        if not header_fields or header_fields[0] != "OFF":
            raise ValueError(f"Not a valid OFF header on line {line_number}")

        count_fields = header_fields[1:]
        if not count_fields:
            line_number, counts = read_data_line()
            count_fields = counts.split()
        if len(count_fields) != 3:
            raise ValueError(f"Invalid OFF counts on line {line_number}")
        try:
            vertex_count, face_count, _ = (int(value) for value in count_fields)
        except ValueError as error:
            raise ValueError(f"Invalid OFF counts on line {line_number}") from error

        vertices: list[vector3] = []
        for _ in range(vertex_count):
            line_number, vertex_line = read_data_line()
            coordinates = vertex_line.split()
            if len(coordinates) < 3:
                raise ValueError(f"Invalid OFF vertex on line {line_number}")
            try:
                vertices.append(vector3(*(float(value) for value in coordinates[:3])))
            except ValueError as error:
                raise ValueError(f"Invalid OFF vertex on line {line_number}") from error

        for _ in range(face_count):
            line_number, face_line = read_data_line()
            fields = face_line.split()
            try:
                face_vertex_count = int(fields[0])
            except (IndexError, ValueError) as error:
                raise ValueError(f"Invalid OFF face on line {line_number}") from error

            if face_vertex_count < 3 or len(fields) < face_vertex_count + 1:
                raise ValueError(f"Invalid OFF face on line {line_number}")

            try:
                vertex_indices = [
                    int(value) for value in fields[1:face_vertex_count + 1]
                ]
            except ValueError as error:
                raise ValueError(f"Invalid OFF face on line {line_number}") from error
            if any(index < 0 or index >= len(vertices) for index in vertex_indices):
                raise ValueError(f"OFF vertex index out of range on line {line_number}")

            color_fields = fields[face_vertex_count + 1:]
            if color_fields and len(color_fields) not in (3, 4):
                raise ValueError(f"Invalid OFF face color on line {line_number}")

            face = Face([vertices[index] for index in vertex_indices])
            if color_fields:
                try:
                    color = [float(value) for value in color_fields]
                except ValueError as error:
                    raise ValueError(
                        f"Invalid OFF face color on line {line_number}"
                    ) from error

                if all(0 <= channel <= 1 for channel in color):
                    color = [round(channel * 255) for channel in color]
                if any(channel < 0 or channel > 255 for channel in color):
                    raise ValueError(f"Invalid OFF face color on line {line_number}")
                if len(color) == 3:
                    color.append(255)
                face.color = pygame.Color(*(int(channel) for channel in color))
            model.add_face(face)
    return model


def read_obj_file(location: str) -> Faces:
    """
    Read vertex positions and polygon faces from a Wavefront OBJ file.

    Texture coordinates, normals, and other OBJ records are ignored. Face
    vertex order is preserved, since it defines the winding used to calculate
    each Face's normal.
    """
    model = Faces()
    vertices: list[vector3] = []

    with open(location, "r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.partition("#")[0].strip()
            if not line:
                continue

            fields = line.split()
            record = fields[0]

            if record == "v":
                if len(fields) < 4:
                    raise ValueError(
                        f"OBJ vertex on line {line_number} must have x, y, and z coordinates"
                    )
                try:
                    vertices.append(vector3(*(float(value) for value in fields[1:4])))
                except ValueError as error:
                    raise ValueError(
                        f"Invalid OBJ vertex on line {line_number}"
                    ) from error
            elif record == "f":
                if len(fields) < 4:
                    raise ValueError(
                        f"OBJ face on line {line_number} must have at least three vertices"
                    )

                face_vertices: list[vector3] = []
                for reference in fields[1:]:
                    try:
                        vertex_index = int(reference.split("/", 1)[0])
                    except ValueError as error:
                        raise ValueError(
                            f"Invalid OBJ face vertex on line {line_number}: {reference}"
                        ) from error

                    if vertex_index == 0:
                        raise ValueError(
                            f"OBJ vertex indices are 1-based on line {line_number}"
                        )

                    resolved_index = (
                        vertex_index - 1 if vertex_index > 0
                        else len(vertices) + vertex_index
                    )
                    if not 0 <= resolved_index < len(vertices):
                        raise ValueError(
                            f"OBJ face vertex index out of range on line {line_number}: {vertex_index}"
                        )
                    face_vertices.append(vertices[resolved_index])

                model.add_face(Face(face_vertices))

    return model
