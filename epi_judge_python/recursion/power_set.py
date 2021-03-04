from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION] P15.5

# Given: S={0,1,2}
# SOLUTION: [0], [1], [2], [0,1], [0,2], ... [0,1,2]

# Time complexity:
#       ~ to number of function calls C(n) per function: C(n) = 2*C(n-1) --> 2^n
#       Total = n * 2^n
# Space complexity = same as time complexity
def generate_power_set(input_set: List[int]) -> List[List[int]]:
    def recurse(i, candidate):
        if i == len(input_set):
            solutions.append(candidate)
            return

        # At each index position i, we either include or not include the element.
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
