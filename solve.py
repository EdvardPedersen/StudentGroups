from collections import defaultdict
from itertools import combinations, groupby
from timeit import default_timer as timer
from solution import Solution
from brute_force import brute_force
from lowest_least_used import lowest_least_used
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solver for class group problem")
    parser.add_argument('--start', type=int, default=6, help="First N to solve")
    parser.add_argument('--stop', type=int, default=8, help="Last N to solve")
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--bf', action='store_true', help="Use the brute-force algorithm")
    parser.add_argument('--llu', action='store_true', help="Use the lowest-least-used heuristic")
    conf = parser.parse_args()

    for i in range(conf.start,conf.stop + 1):
        if conf.llu:
            start = timer()
            print("HEURISTIC:")
            lowest_least_used(i, 3)[0].pretty_print(verbose = True)
            end = timer()
            print("Time taken for {} students: {}".format(i, end-start))
        if conf.bf:
            start = timer()
            print("BRUTE-FORCE:")
            solutions = brute_force(i, 3)
            solutions[0].pretty_print(verbose = True)
            print("{} optimal solutions found of length {}".format(len(solutions), solutions[0].length))
            end = timer()
            print("Time taken for {} students: {}".format(i, end-start))

