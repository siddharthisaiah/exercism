from itertools import permutations

def equilateral(sides):
    return triangle_equality(sides) and len(set(sides)) == 1


def isosceles(sides):
    return triangle_equality(sides) and len(set(sides)) <= 2


def scalene(sides):
    return triangle_equality(sides) and len(set(sides)) == 3


def triangle_equality(sides):
    if any(sides) <= 0:
        return False
    
    side_perms = [x for x in set(permutations(sides))]
    for n in side_perms:
        if not (n[0] + n[1] >= n[2]): return False
    return True
