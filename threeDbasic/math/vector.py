from math import sqrt,cos,sin

class vector3():
    """
    my implementation of 3d vector. 
    multiplication as a cross product.
    """

    def __init__(self, x:float, y:float, z:float):
        """
        initialization 3d vector.
        """
        self.x:float = x
        self.y:float = y
        self.z:float = z
        self.iter = 0
    
    def dot_product(self, other) -> float:
        """
        returns a dot product of two 3d vector.
        calculation is done by manual, so maybe some amount of overhead can be exist.
        """
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross_product(self, other):
        """
        calculate cross product.
        note that sign follows right hand rule.
        """
        return vector3(self.y*other.z - self.z*other.y, self.z * other.x - self.x * other.z, self.x * other.y - self.y * other.x)

    def mul_scalar(self, scalar:float):
        """
        returns a vector multiplied by scalar. 
        does not modifies original vector.
        """
        return vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def change(self, x:float, y:float, z:float):
        """
        changes x, y, z values immediately to save RAM.
        """
        self.x, self.y, self.z = x, y, z

    def size(self)->float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def size_squared(self)->float:
        return self.x**2 + self.y**2 + self.z**2

    def normalize(self):
        return vector3(self.x, self.y, self.z) / self.size()

    def projection(self, other):
        return self.dot_product(other) * other

    def to_3d_tuple(self) -> tuple[float,float,float]:
        return (self.x, self.y, self.z)

    def to_2d_tuple(self) -> tuple[float,float]:
        return (self.x, self.y)
    
    

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.mul_scalar(other)
        elif isinstance(other, vector3):
            return self.cross_product(other)
        else:
            raise TypeError("uncorrect type in vector3 multiplication!")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def add(self, other):
        return vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __add__(self, other):
        return self.add(other)

    def __radd__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        return self.add(other)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __sub__(self, other):
        return self.add(-1 * other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.mul_scalar(1/other)
        raise TypeError("vector cannot be divided by vector or else.")

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    
    def __iter__(self):
        return self

    def __next__(self):
        self.iter += 1
        match self.iter:
            case 1:
                return self.x
            case 2:
                return self.y
            case 3:
                return self.z
            case _:
                raise StopIteration

    def __getitem__(self, key):
        match key:
            case 0:
                return self.x
            case 1:
                return self.y
            case 2:
                return self.z
            case _:
                raise IndexError(f"vector 3 has only 3 item! {key} index is not good!")

# vector constants.
e1 = vector3(1,0,0)
e2 = vector3(0,1,0)
e3 = vector3(0,0,1)

def cross(v1:vector3, v2:vector3):
    """
    calculate cross product and returns.
    v1 and v2 are not modified.
    """
    return v1.cross_product(v2)

def dot(v1:vector3, v2:vector3):
    """
    calculate dot product and return
    """
    return v1.dot_product(v2)

def rotation_throuh_axis(v:vector3, axis:vector3, angle:float) -> vector3 :
    """
    rotation using formular.
    """
    return v + sin(angle) * (axis * v) + (1-cos(angle)) * axis * (axis * v)

def angle_diff(v1:vector3, v2:vector3, zeortopi = True) -> float:
    """
    if zerotopi is false, returns value in range(-pi/2, pi/2). might be more useful
    """
    from math import acos, pi
    ret =  acos(dot(v1, v2) / v1.size() / v2.size())
    if zeortopi:
        return ret
    elif ret <= pi/2:
        return ret
    return pi/2 - ret
