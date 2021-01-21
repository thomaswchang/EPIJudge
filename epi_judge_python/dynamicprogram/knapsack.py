import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# [PROBLEM_TYPE=DP]
# Step1: How to recognize a problem is a DP? What is the recurrence?
#   The optimum solution at weight depends on [ weight-statue1, .. , weight-statue2]

# Step2: Decide the state. What is the key to the lookup table?
#    States IS used as (1) input recursive function parameter (2) the row & col of matrix.
#
#   This problem does not have a table, but use recursion. Since it uses recursion, r goes from hi -> lo unlike the American football combination (number_of_score_comb.py)
#
#   State
#       r = selection of clocks,
#       c = curr weight in knapsack
#   Constraints: weightLeft, k

# Step3: Formulate a relation among the states
#   value[r][w] = max( value[r-1][w], value[r-1][w-w@r] + v@r]

# Step4:  Optimize by adding tabulation or memoization

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:

    #returns optimum value for state (i, available_capacity)
    @functools.lru_cache(None)
    def recurse(i: int, available_capacity: int) -> int :
        if i < 0: # i represent the row of our grid, even if we don't have a grid.
            return 0

        without_this_item = recurse(i-1, available_capacity)

        # Break ternary assignmnet to be more readable
        with_item = 0
        if available_capacity >= items[i].weight:
            with_item =  items[i].value + recurse(i-1, available_capacity - items[i].weight)

        return max(without_this_item, with_item)

    return recurse(len(items) -1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
