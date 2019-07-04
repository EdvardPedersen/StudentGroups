from collections import defaultdict
from solution import Solution

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


def lowest_least_used(number, selections):
    students = range(1,number+1)
    permutations = generate_combinations(students, selections)

    return [Solution(permutations, students)]
