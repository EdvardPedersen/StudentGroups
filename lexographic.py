from collections import defaultdict
from itertools import combinations
from solution import Solution

def lexographic(number, selections):
    # Generate a list of all participants
    students = range(1,number+1)

    # Generate all combinations (k choose 3)
    combs = list(combinations(students, selections))

    # Always start with the lexographically first combination
    current = [combs[0]]

    # Iterate over all combinations after first
    for el in combs[1:]:
        # Verify that this combination is legal to select
        new = set(el)
        legal = True
        for elem in current:
            if len(new.intersection(elem)) >= 2:
                legal = False

        # Only add this to the list, if it is actually legal to add
        if legal:
            current.append(el)

    return [Solution(current, students)]
