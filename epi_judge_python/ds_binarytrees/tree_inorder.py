from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

# PROBLEM_TYPE=BINARYTREE

class BinaryTreeNode():
    def __init__(self, data = None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result = []

    from collections import deque
    queue = deque( [(tree, False)])

    while queue:
        node, left_subtree_traversed = queue.popleft()
        if node:
            if left_subtree_traversed:
                result.append(node.data)
            else:
                queue.append((node.left, False))
                queue.append((node, True))
                queue.append((node.right, False))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
