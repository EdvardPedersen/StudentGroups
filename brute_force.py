from itertools import combinations, groupby
from solution import Solution

def compare_sequence(seq1, seq2):
    for a, b in zip(seq1, seq2):
        for z,x in zip(a, b):
            if z != x:
                return False
    return True

def brute_force(number, selections):
    students = range(1, number + 1)
    comb = list(combinations(students, selections))
    solutions = []
    for c in comb:
        solutions.extend(brute_recurse([c], [x for x in comb if x not in [c]], ))

    solutions = sort_solutions(solutions)

    max_len = 0
    optimal_solutions = []
    last_solution = []
    for solution in solutions:
        if len(solution) > max_len:
            max_len = len(solution)
            optimal_solutions = []
            optimal_solutions.append(solution)
            last_solution = solution
        elif len(solution) == max_len and not compare_sequence(solution, last_solution):
            optimal_solutions.append(solution)
            last_solution = solution
    solution_list = []
    for solution in optimal_solutions:
        solution_list.append(Solution(solution, students))
    return solution_list

def sort_solutions(solutions):
    for solution in solutions:
        for i, triple in enumerate(solution):
            solution[i] = tuple(sorted(triple))
        solution.sort(key=str)

    return sorted(list(x for x,_ in groupby(solutions)))


def brute_recurse(current, remaining):
    recursed = 0
    solutions = []
    legal_remaining = [x for x in remaining if check_legal(x, current)]
    for elem in legal_remaining:
        solutions.extend(brute_recurse(current + [elem], [x for x in legal_remaining if not x in [elem]]))
        recursed = True
    if not recursed:
        return [current]
    return solutions

def check_legal(new, current):
    for elem in current:
        s = 0
        for item in new:
            s += elem.count(item)
        if s > 1:
            return False
    return True
