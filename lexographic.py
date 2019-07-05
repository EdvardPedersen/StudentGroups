from collections import defaultdict
from itertools import combinations
from solution import Solution

def check_legal(new, current):
    for elem in current:
        if new[0] in elem:
            if new[1] in elem or new[2] in elem:
                return False
        if new[1] in elem and new[2] in elem:
            return False
    return True


def lexographic(number, selections):
    students = range(1,number+1)
    combs = list(combinations(students, selections))
    current = [combs[0]]
    for el in combs[1:]:
        if check_legal(el, current):
            current.append(el)

    return [Solution(current, students)]
