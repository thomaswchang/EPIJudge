from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION]

def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def recurse(i, candidate):
        if i == len(input_set):
            solutions.append(candidate)
            return

        recurse(i+1, candidate)
        recurse(i+1, candidate + [input_set[i]])

    solutions : List[List[int]] = []

    recurse(0, [])

    return solutions


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
