from collections import defaultdict
from itertools import combinations, groupby
from timeit import default_timer as timer

class Solution():
    def __init__(self, sequence, students):
        self.sequence = sequence
        self.length = len(sequence)
        self.counts = dict()
        for s in students:
            self.counts[s] = 0
        for seq in sequence:
            for elem in seq:
                self.counts[elem] += 1
        self.min_count = min(self.counts.values())
        self.students = students

    def pretty_print(self, verbose = False):
        print("Number of students: {}".format(len(self.students)))
        print("Number of valid groups in solution: {}".format(self.length))
        print("Minimum number of groups an individual can participate in: {}".format(self.min_count))
        print("-----------------------------------------------------------------")
        if verbose:
            print(self.sequence)
            for n in self.counts:
                print("Student {} participates in {} groups".format(n, self.counts[n]))
            print("-----------------------------------------------------------------")



def legal_permutation(permutation, already_paired):
    for elem in permutation:
        for check in permutation:
            if elem in already_paired[check]:
                return False
    return True

def pair_combination(permutation, already_paired):
    for i in permutation:
        for elem in [x for x in permutation if x != i]:
            already_paired[i].append(elem)


def generate_combinations(students, selections):
    used = dict()
    links = defaultdict(list)
    for elem in students:
        used[elem] = 0
        links[elem].append(elem)
    fails = 0
    exclusion = []
    results = []
    while fails < 10:
        temp_list = []
        for _ in range(selections):
            current_item = get_least_used(exclusion, used)
            exclusion.extend(links[current_item])
            temp_list.append(current_item)
        if None not in temp_list:
            results.append(tuple(temp_list))
            fails = 0
        else:
            fails += 1
            exclusion = []
            continue
        for i in temp_list:
            used[i] += 1
            newlist = [x for x in temp_list if x != i]
            for elem in newlist:
                links[i].append(elem)
    return results

def get_least_used(exclusion, used):
    min_value = 1000
    item_value = 0
    for item in sorted(used.keys()):
        if item in exclusion:
            continue
        if used[item] < min_value:
            min_value = used[item]
            item_value = item
    if item_value == 0:
        return None
    return item_value



def get_students(number, selections):
    students = range(1,number+1)
    permutations = generate_combinations(students, selections)

    return [Solution(permutations, students)]

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
        solution.sort(key=lambda x: x[0]*100 + x[1]*10 + x[2])

    return sorted(list(x for x,_ in groupby(solutions)))


def brute_recurse(current, remaining):
    recursed = 0
    solutions = []
    for elem in remaining:
        if check_legal(elem, current):
            solutions.extend(brute_recurse(current + [elem], [x for x in remaining if not x in [elem]]))
            recursed = True
    if not recursed:
        return [current]
    return solutions

def check_legal(new, current):
    for elem in current:
        if new[0] in elem:
            if new[1] in elem or new[2] in elem:
                return False
        if new[1] in elem and new[2] in elem:
            return False
    return True

for i in range(6,8,1):
    start = timer()
    #get_students(i, 3)
    solutions = brute_force(i, 3)
    for solution in solutions:
        solution.pretty_print(verbose = True)
        pass
    print("{} optimal solutions found of length {}".format(len(solutions), solutions[0].length))
    end = timer()
    print("Time taken for {} students: {}".format(i, end-start))

