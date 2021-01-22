class BinaryTreeNode():
    def __init__(self, data = None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



# root -> left -> right
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:
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
                queue.append((node.right, False))
                queue.append((node, True))

    return result
