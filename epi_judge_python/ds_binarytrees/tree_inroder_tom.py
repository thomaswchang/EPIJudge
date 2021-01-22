

import collections

class BinaryTreeNode():
    def __init__(self, data = None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# is binary search tree?  inorder traveral with binary search syntax
# In order: Left -> root --> right
def viaIterationV1(tree: BinaryTreeNode) :
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


# in order: root.left -> root.val -> root.right
def viaIterationV2(root, k):
    from collections import deque
    stack = deque()

    while True:
        while root:
            stack.append(root)
            root = root.left

        root.pop() # returns the most left element; smallest element in the tree

        # embed business logic here
        k = k-1
        if not k:
            return root.val

        root = root.right

def viaRecursion(root):
    return viaRecursion(root.left) + [root.val] + viaRecursion(root.right) if root else []

