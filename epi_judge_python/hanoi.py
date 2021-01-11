import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

# [PROBLEM_TYPE=RECURSION]
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:

    # Work through a couple of examples
    # Hint: If I know how to move the n-1 peg, what does the nth peg move look like?

    # Big O Analysis
    #   Run time: 2^n
    #       T(n) = T(n-1) + 1 + T(n-1)
    #       first T(n-1) is for the n-1th peg; 2nd T(n-1) is for the final move. Since we can only move one block at a time.
    #       T(n) = 1 + 2, +4 + 2^k * T(n-k) = 2^n

    # from_peg: the peg we move blocks from
    # to_peg: the peg we move our block TO
    # use_peg: the peg we use as an intermediary step
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg,
                                  use_peg):
        print(f"num_rings_to_move={num_rings_to_move} from_peg={from_peg} to_peg={to_peg} use_peg={use_peg}")
        if num_rings_to_move > 0:
            # This represents how we move the n-1 th peg. In this iteration, we use_peg and to_peg are "flipped" from the final desired state
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg=from_peg, to_peg=use_peg, use_peg=to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg=use_peg, to_peg=to_peg, use_peg=from_peg)
        #print(f"result={result}")

    # Initialize pegs.
    result: List[List[int]] = []
    pegs = [list(reversed(range(1, num_rings + 1))) # pegs is a nested array of 3 inner arrays. Each inner array represent one peg.
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    # pegs represents what block is in each of the 3 PEGS. The size of the block is represented by
    pegs = [list(reversed(range(1, num_rings + 1)))] \
           + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
