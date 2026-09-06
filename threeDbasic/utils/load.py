from threeDbasic.base.faces import faces, face
from threeDbasic.math.vector import vector3

def read_off_file(location: str, globalty = False) -> faces:
    """
    reads off file at given location.

    note that file looks like

    `
    OFF
    4(vertice num) 4(face num) 4(edge number)
    vertices points as x, y, z.
    ...
    faces with vertices
    
    
    `

    """
    model = faces()
    with open(location, "r", encoding="UTF-8") as file:
        def read_with_ignoring_comments() -> str:
            raw = file.readline().strip()
            if raw.find("#") == -1:
                return raw
            return raw.split("#")[0].strip()

        
        if 'OFF' != read_with_ignoring_comments():
            # checks if file is valid.
            # wait... from wiki, OFF file can be valid without this praise?
            # just think as this is standard. BRR...
            # also, note that '#' should be ignored...
            raise ValueError('Not a valid OFF header')
        vertice_num, face_num, edge_num = tuple([int(s) for s in read_with_ignoring_comments()])
        vertices = [vector3(*(float(s) for s in read_with_ignoring_comments())) for _ in range(vertice_num)]

        for _ in range(face_num):
            cur_face = face()
            cur_line = read_with_ignoring_comments()
            # format with 7 i j k l m ...
            for i in cur_line.split(" ")[1:]:
                cur_face.add_point(vertices[int(i)])
            model.add_face(cur_face)
    return model

