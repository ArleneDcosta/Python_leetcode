class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_bst(root):
    if root is None:
        return None

    # Swap left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert left and right subtrees
    invert_bst(root.left)
    invert_bst(root.right)

    return root

# Helper function to print in-order traversal of the tree
def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

# Example usage
if __name__ == "__main__":
    # Constructing BST
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original BST (in-order traversal):")
    inorder_traversal(root)
    print()

    # Inverting the BST
    invert_bst(root)

    print("Inverted BST (in-order traversal):")
    inorder_traversal(root)
    print()
