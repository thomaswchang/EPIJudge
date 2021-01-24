from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from collections import namedtuple

# [PROBLEM_TYPE=BINARYTREE] P116

def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    StatusWithHeight = namedtuple('StatusWithHeight', ('bBalanced', 'height'))

    def check_height(node) -> StatusWithHeight :

        if not node:
            return StatusWithHeight(True, -1)

        bLeftStatus = check_height(node.left)
        if not bLeftStatus.bBalanced:
            return bLeftStatus

        bRightStatus = check_height(node.right)
        if not bRightStatus.bBalanced:
            return bRightStatus

        is_balanced = abs(bLeftStatus.height - bRightStatus.height) <= 1

        height = max(bLeftStatus.height, bRightStatus.height) +1

        return StatusWithHeight(is_balanced, height)

    return check_height(tree).bBalanced

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
