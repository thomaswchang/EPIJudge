from typing import List

from test_framework import generic_test

# [PROBLEM_TYPE=DP PG 253]

# Given a 2D matrix, and a 1D array of integers pattern, determine if the pattern can be traversed in sequence from the matrix

# Step1: How to recognize a problem is a DP? What is the recurrence?
# Not sure if this is a DP problem, since there is no optimum solution; it's just recurrence

# Step2: Decide the state. What is the key to the lookup table?
# state:
#   current x, y in grid
#   ith offset to pattern

# Step3: Formulate a relation among the states

# Step4:  Optimize by adding tabulation or memoization

# grid is a square
def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:

    def recurse(x, y, i):
        if len(pattern) == i:
            return True

        if not ( (0 <= x <len(grid)) and (0<= y <len(grid[x])) ) or grid[x][y] != pattern[i] :
            return False

        return any( [recurse(position[0], position[1], i+1) for position in ( (x-1, y), (x+1, y), (x, y-1), (x, y+1))])


    return any(
        [ recurse(r, c, 0) for r in range(len(grid)) for c in range(len(grid[r])) ]
    )



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
