from threeDbasic.base.constants import EPSILONE

def is_similar(a, b, epsilon = EPSILONE) -> bool:
    """
    checks if a and b are similar in given epsilon
    note that a and b should be substractable
    """
    return (abs(a - b) <= epsilon)