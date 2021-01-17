from typing import List

from test_framework import generic_test, test_utils

# [PROBLEM_TYPE=RECURSION]

# Generate all permutation of an array
# Given [2,3,5,7] -> [2,3,5,7], [2,5,3,7]
def permutations(A: List[int]) -> List[List[int]]:
    # Runtime:
    #   proportional to number of function calls C(n) = 1 + n C(n-1) --> n * n!
    def recurse(i):
        if i == len(A)-1:
            solutions.append(A.copy()) #shallow copy of non-compound object is will create independent copies
            return

        for j in range(i, len(A)): # n
            A[i], A[j] = A[j], A[i] # swap
            recurse(i+1) # C(n-1) => n!
            A[i], A[j] = A[j], A[i] # backtrack

    solutions: List[List[int]] = []
    # candidate = [] # we do not need candidate because we will just reuse the
    recurse(0)
    return solutions

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
