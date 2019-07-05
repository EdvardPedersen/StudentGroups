import argparse
from collections import defaultdict
from itertools import combinations, groupby
from timeit import default_timer as timer
from solution import Solution
from brute_force import brute_force
from lowest_least_used import lowest_least_used
from lexographic import lexographic


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solver for class group problem")
    parser.add_argument('--start', type=int, default=6, help="First N to solve")
    parser.add_argument('--stop', type=int, default=8, help="Last N to solve")
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--print_all', action='store_true')
    parser.add_argument('--bf', action='store_true', help="Use the brute-force algorithm")
    parser.add_argument('--llu', action='store_true', help="Use the lowest-least-used heuristic")
    parser.add_argument('--lex', action='store_true', help="Use the lexographic heuristic")
    parser.add_argument('--group_size', type=int, default=3, help="Group size to use")
    conf = parser.parse_args()

    for i in range(conf.start,conf.stop + 1):
        if conf.lex:
            start = timer()
            print("HEURISTIC - LEXOGRAPHIC:")
            lexographic(i, conf.group_size)[0].pretty_print(conf.verbose)
            end = timer()
            print("Time taken for {} students: {}".format(i, end-start))
        if conf.llu:
            start = timer()
            print("HEURISTIC - LOWEST LEAST USED")
            lowest_least_used(i, conf.group_size)[0].pretty_print(conf.verbose)
            end = timer()
            print("Time taken for {} students: {}".format(i, end-start))
        if conf.bf:
            start = timer()
            print("BRUTE-FORCE:")
            solutions = brute_force(i, conf.group_size)
            if conf.print_all:
                for solution in solutions:
                    solution.pretty_print(conf.verbose)
            else:
                solutions[0].pretty_print(conf.verbose)
            print("{} optimal solutions found of length {}".format(len(solutions), solutions[0].length))
            end = timer()
            print("Time taken for {} students: {}".format(i, end-start))

