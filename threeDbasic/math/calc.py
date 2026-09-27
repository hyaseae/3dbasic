from threeDbasic.base.constants import EPSILONE
from threeDbasic.math.vector import vector3, det1, det2
from math import sqrt,cos,sin

def is_similar(a, b, epsilon = EPSILONE) -> bool:
    """
    checks if a and b are similar in given epsilon
    note that a and b should be substractable
    """
    return (abs(a - b) <= epsilon)


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

def is_similar_vector(a:vector3, b:vector3, epsilon=EPSILONE):
    """
    check if two vector is similar.
    """

    return (a - b).size_squared() <= epsilon

def custom_det(a0: vector3, a1: vector3, a2: vector3):
    return dot(a0, cross(a1, a2))


def cramers_rule(a0: vector3, a1: vector3, a2: vector3, b: vector3) -> vector3:
    """
    solves linear equation using cramer's rule.
    """
    ans = vector3(0, 0, 0)
    for i in range(3):
        ax:list[vector3] = [a0, a1, a2]
        ax[i] = b
        ans[i] = custom_det(*ax) / custom_det(a0, a1, a2)
    return ans