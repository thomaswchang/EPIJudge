from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# [PROBLEM_TYPE=STACKQUEUE]

#class BinaryTreeNode:
#    def __init__(self, data, left=None, right=None):
#        self.data = data
#        self.left = left
#        self.right = right

def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    queue = [tree]
    result: List[ List[int]] = []
    if not tree:
        return result

    while queue:
        result.append([node.data for node in queue])

        # Update queue using nested list comprehension
        queue = [child for node in queue
            for child in (node.left, node.right) if child]

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
