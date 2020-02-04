class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


def count_unival_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_unival_trees(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_unival_trees(root.left)

    child_counts = count_unival_trees(root.left) + count_unival_trees(root.right)

    if root.data == root.left.data and root.data == root.left.data:
        child_counts += 1
    
    return child_counts