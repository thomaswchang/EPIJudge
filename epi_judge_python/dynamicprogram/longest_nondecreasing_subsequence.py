from typing import List

from test_framework import generic_test

# [PROBLEM_TYPE=DP]

# Return the LENGTH of the longest NON-DECREASING subsequence in a sequence of integer
# Example:
#   Input: A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]
#   Solution: 4 ; [0, 8, 12,14], [0,2,6,9], [0,4,6,9]

# Step1: How to recognize a problem is a DP? What is the recurrence?

# Step2: Decide the state. What is the key to the lookup table?
#   (count)

# Step3: Formulate a relation among the states
#   L[0] = 1
#   L[1] -> L[1]>L[0] -> 1 + L[0] = 2
#   L[2] -> L2 > L0 -> 1 + L0 = 2
#   L3 -> L3 > [L0, L1, L2] -> 1 + max([L0, L1, L2] ) = 3
#   L_i -> 1 + max( L[j] for j in range(i) if L[i] >= L[j])

# Step4:  Optimize by adding tabulation or memoization
#   Traverse from left to right; in comparison a tabulation would go from upperLeft --> lowerRight, or vice versa for recursive

def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    max_length = [1] * len(A)

    for i in range(len(A)):
        max_length[i] = 1 + \
                        max(
                            [ max_length[j] for j in range(i) if A[i] >= A[j] ],
                            default=0 # if the array is empty, then max returns 0
                        )

    return max(max_length)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
