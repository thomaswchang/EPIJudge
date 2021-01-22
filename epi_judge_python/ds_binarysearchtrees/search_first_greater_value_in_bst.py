from typing import Optional

from bst_node import BstNode
from test_framework import generic_test

# TYPE=BINARYSEARCHTREE PG 206

# Given a BST and input value, find the first number greater than the input value.

class BstNode():
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    next_node, candidate_node = tree, None

    while next_node:
        if next_node.data < k:
            next_node, candidate_node = next_node.left, next_node
        else:
            next_node = next_node.right

    return candidate_node


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
