class BinaryTree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def minDepth(root):
    if root is None: return None
    if root.left is None and root.right is None: return 0
    if root.left is None: return 1 + minDepth(root.right)
    if root.right is None: return 1 + minDepth(root.left)

    return 1 + min(minDepth(root.left), minDepth(root.right))


