from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# PROBLEM_TYPE=BINARYTREE P122

# Given a tree and an integer X, check if there is a path from ROOT to LEAF that sums up to the integer X

def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    if not tree:
        return False

    if not tree.left and not tree.right: # check leaf
        return remaining_weight == 0

    return has_path_sum(tree.left, remaining_weight-tree.data) or has_path_sum(tree.right, remaining_weight.data)

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
