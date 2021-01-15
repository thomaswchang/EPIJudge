import copy
import functools
import itertools
import math
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# [PROBLEM_TYPE=RECURSION]

def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    def iterate(r, c) -> bool:
        if r == numRows:
            r = 0
            c +=1
            if c >= numCols: # base condition
                return True

        if partial_assignment[r][c] != 0:
            return iterate(r +1, c)

        def checkIsValid(r,c, val):
            # Check for row constrants
            if any(val == partial_assignment[k][c] for k in range(numRows)):
                return False

            if any(val == partial_assignment[r][k] for k in range(numCols)):
                return False

            region_size = int(math.sqrt(len(numRows)))
            R = r // numRows
            C = c // numCols
            if any(val == partial_assignment[R+a][C+b] for a, b in itertools.product(range(region_size))):
                return False

            return True

        for val in range(1, numRows+1):
            if checkIsValid(r, c, val):
                partial_assignment[r][c] = val
                if iterate(r+1, c):
                    return True

        partial_assignment[r][c] = 0


    numRows = len(partial_assignment)
    numCols = len(partial_assignment[0])
    return iterate(0, 0)


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
