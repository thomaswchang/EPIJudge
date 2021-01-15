from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION]


# Time complexity:
#       ~ to number of function calls C(n) per function: C(n) = 2*C(n-1) --> 2^n
#       Total = n * 2^n
# Space complexity = same as time complexity
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
