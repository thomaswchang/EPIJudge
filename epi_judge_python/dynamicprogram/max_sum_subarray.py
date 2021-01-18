from typing import List

from test_framework import generic_test

# [PROBLEM_TYPE=DP] PG 244

# Find the max sum over all subarrays given array of integers
# Input:    A = [-2, 3, 1, -7, 3, 2, -1]
#           B = [-2, 3, 4, -4, 3, 5, 4]  --> expected=4

def find_maximum_subarray(A: List[int]) -> int:

    maxCurr, maxAll = 0, 0

    for a in A:
        maxCurr = max(a, a + maxCurr)
        maxAll = max(maxAll, maxCurr)

    return maxAll


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
