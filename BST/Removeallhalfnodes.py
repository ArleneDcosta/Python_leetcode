
# Python program to remove all half nodes

# A binary tree node
class Node:
    # Constructor for creating a new node
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

# For inorder traversal
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print root.data,
        printInorder(root.right)

# Removes all nodes with only one child and returns
# new root(note that root may change)
def RemoveHalfNodes(root):
    if root is None:
        return None

    # Recur to left tree
    root.left = RemoveHalfNodes(root.left)
    
    # Recur to right tree
    root.right = RemoveHalfNodes(root.right)
    
    # if both left and right child is None
    # the node is not a Half node
    if root.left is None and root.right is None:
        return root

    # If current nodes is a half node with left child
    # None then it's right child is returned and
    # replaces it in the given tree
    if root.left is None:
        new_root = root.right
        temp = root
        root = None
        del(temp)
        return new_root

    if root.right is None:
        new_root = root.left
        temp = root
        root = None
        del(temp)
        return new_root
    
    return root

# Driver Program
root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

print "Inorder traversal of given tree"
printInorder(root)

NewRoot = RemoveHalfNodes(root)

print "\nInorder traversal of the modified tree"
printInorder(NewRoot)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
