from test_framework import generic_test

# [PROBLEM_TYPE=DP PG 250]

# Given a matrix, return HOW many different ways of starting from top-left to bottom-right
#

# Step1: How to recognize a problem is a DP? What is the recurrence?
# Each position x,y = pos(x-1, y) + pos(x, y-1)

# Step2: Decide the state. What is the key to the lookup table?
#   state position x,y


# Step3: Formulate a relation among the states

# Step4:  Optimize by adding tabulation or memoization


def number_of_ways_via_recursion(n: int, m: int) -> int:
    def recurse(x, y):
        if x==0 and y==0:
            return 1

        from_top = 0 if x == 0 else recurse(x-1, y)
        from_left = 0 if y==0 else recurse(x, y-1)

        return from_top + from_left
    return recurse(n-1, m-1)


def number_of_ways_via_recursion(n: int, m: int) -> int:
    # grid_incorrect = [[0] * n] * m # * m will create m shallow copies; when I update one row, it will update all 3 rows!!!
    grid = [[0]*n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            if r==0 or c==0:
                grid[r][c] = 1

    for r in range(1, m):
        for c in range(1, n):
            grid[r][c] = grid[r-1][c] + grid[r][c-1]

    return grid[m-1][n-1]




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways_via_recursion))
