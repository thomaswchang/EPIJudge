from typing import List

from test_framework import generic_test, test_utils

# TYPE=BINARYSEARCHTREE P207

# Brute force method would be do a in order traversal and return the top n elements. Not the most efficient.

class BstNode():
    def __init__(self, data = None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:

    def recurse(tree):
        if tree and len(k_largest) < k:
            recurse(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data) # if reached here the first time, we have already reach the most right
                recurse(tree.left)

    k_largest = []
    recurse(tree)
    return k_largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
