import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import collections

# PROBLEM_TYPE=BINARYTREE PG 120

def lca(tree: BinaryTreeNode,
        node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    Status = collections.namedtuple('Status', ('num_occurences_in_subtree', 'ancestor'))

    def recurse(tree, node0, node1) -> Status:
        if tree is None:
            return Status(num_occurences_in_subtree=0, ancestor=None)

        left_status = recurse(tree.left, node0, node1)
        if left_status.num_occurences_in_subtree == 2:
            return left_status

        right_status = recurse(tree.right, node0, node1)
        if right_status.num_occurences_in_subtree == 2:
            return right_status

        num_total_occurences = \
            left_status.num_occurences_in_subtree + \
            right_status.num_occurences_in_subtree + (node0, node1).count(tree)

        return Status(num_total_occurences, tree if num_total_occurences==2 else None)

    return recurse(tree, node0, node1).ancestor


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
