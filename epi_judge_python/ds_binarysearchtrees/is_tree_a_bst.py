from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import collections

# TYPE=BINARYSEARCHTREE

def viaRecursion(tree: BinaryTreeNode) -> bool:
    def recurse(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        elif not (low <= node.data <= high):
            return False
        return (
            recurse(node.left, low, node.data) and
            recurse(node.right, node.data, high)
        )

    recurse(tree)

def viaIteration(tree: BinaryTreeNode) :
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque( [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        current = bfs_queue.popleft()

        if current.node:
            # Business logic
            if not current.lower <= current.node.data <= current.higher:
                return False

            bfs_queue.extend(
                (
                    QueueEntry(current.node.left, current.lower, current.node.data),
                    QueueEntry(current.node.right, current.node.data, current.lower)
                )
            )
    return True

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    return viaIteration(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
