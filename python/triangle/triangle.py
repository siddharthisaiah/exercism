def equilateral(sides):
    return triangle_equality(sides) and len(set(sides)) == 1


def isosceles(sides):
    return triangle_equality(sides) and len(set(sides)) <= 2


def scalene(sides):
    return triangle_equality(sides) and len(set(sides)) == 3


def triangle_equality(sides):
    for l in sides:
        if l <= 0: return False

    if not (sides[1]+ sides[2] >= sides[0]):
        return False
    if not (sides[2]+ sides[0] >= sides[1]):
        return False
    if not (sides[0]+ sides[1] >= sides[2]):
        return False

    return True
