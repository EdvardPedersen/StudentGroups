from collections import defaultdict
from itertools import combinations

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
    taken = defaultdict(list)
    accepted_perm = list()
    groups = dict()
    for s in students:
        groups[s] = 0

    for perm in permutations:
        #if not legal_permutation(perm, taken):
        #    continue
        #pair_combination(perm, taken)
        accepted_perm.append(perm)

        for elem in perm:
            groups[elem] += 1
    print("Number of students: {}".format(len(students)))
    print("Number of valid groups: {}".format(len(accepted_perm)))
    print("Minimum number of groups an individual can participate in: {}".format(min(groups.values())))
    print("-----------------------------------------------------------------")
    print(accepted_perm)
    for n in groups:
        print("{} - {}".format(n, groups[n]))


for i in range(6,200,1):
    get_students(i, 3)

