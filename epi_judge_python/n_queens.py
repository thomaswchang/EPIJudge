from typing import List

from test_framework import generic_test

# [PROBLEM_TYPE=RECURSION]

def n_queens(n: int) -> List[List[int]]:
    def helper(row):
        if row == n:
            solutions.append(col_placement.copy()) # This is a shallow copy, but this is OK since we don't have compound objects.
            return
        else:
            # Iterate through each column: 0, 1, 2, n-1
            for cur_col in range(n):
                # This is the reason why we need only 1 copy of col_placement, even after we get a correct solution.
                # Let assume we have a solution in the prev cur_col-1 loop.  When we revisit the cur_col in range(n) loop,
                # we rewrite col_placement  from curr_col.  This similar logic happens for row; why we don't need to recreated every row solution path.

                if all(
                    # (col_of_prev_queens-cur_col=0) -> we had a queen in the same column for previous rows
                    # (col_of_prev_queens-cur_col=row-i) -> previous row had a diagonal with cur
                    abs(col_of_prev_queens - cur_col) not in (0, row-i)
                    for  i, col_of_prev_queens in enumerate(col_placement[:row]) # c = col of previously placed queen
                ):
                    col_placement[row] = cur_col # We are REUSING col_placement for each row,col
                    helper(row + 1)

    solutions = []

    # col_placement represent placed queens. Each index to col_placement represents a row.
    # col_placement[2] = 3 means the 2nd row has a queen placed at the 3rd column.
    col_placement = [0] * n # reuse this array for all temporary solution. col_placement[row] = col
    helper(0)
    return solutions


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
