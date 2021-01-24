from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# PROBLEM_TYPE=BINARYTREE P 151

# If each node in a binrary has a [0,1] value, find the binary value from root to leaf
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:

    def recurse(node: BinaryTreeNode, curr_sum=0) -> int:
        if not node:
            return 0

        curr_sum = curr_sum*2 + node.data

        if not node.left and not node.right: # leaf node has no value
            return curr_sum

        return recurse(node.left, curr_sum) + recurse(node.right, curr_sum)

    return recurse(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
