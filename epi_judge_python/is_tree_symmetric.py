from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

# [PROBLEM_TYPE=BINARYTREE]

def is_symmetric(tree: BinaryTreeNode) -> bool:

    def check(tree1, tree2) -> bool :
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2:
            return (
                tree1.data == tree2.data and
                check(tree1.left, tree2.right) and
                check(tree1.right, tree2.left)
            )
        return False
    
    return check(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
