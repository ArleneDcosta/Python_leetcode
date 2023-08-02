# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Function to perform inorder traversal on a given binary tree
def inorder(root):
 
    if root is None:
        return
 
    inorder(root.left)
    print root.data,
    inorder(root.right)
 
 
# Function to sink root node having value 0 at the bottom of the tree.
# The left and right subtree (if any) of the root node are already sinked
def sink(root):
 
    # base case: tree is empty
    if root is None:
        return
 
    # if the left child exists and has a non-zero value 
    if root.left and root.left.data:
        # swap the current node data with its left child
        temp = root.data
        root.data = root.left.data
        root.left.data = temp
 
        # recur for the left subtree
        sink(root.left)
 
    # if the right child exists and has a non-zero value
    elif root.right and root.right.data:
        print("inside right",root.data)
        # swap the current node data with its right child
        temp = root.data
        root.data = root.right.data
        root.right.data = temp
 
        # recur for the right subtree
        sink(root.right)
 
 
# The main function to sink nodes having zero value at the bottom
# of the binary tree
def sinkNodes(root):
 
    # base case: tree is empty
    if root is None:
        return
 
    # fix left and right subtree first
    sinkNodes(root.left)
    print("inside main sink")
    sinkNodes(root.right)
 
    # sink the current node if it has a value of 0
    if root.data == 0:
        sink(root)
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
              0
            /   \
           /     \
          1       0
                /   \
               /     \
              0       2
            /   \
           /     \
          3       4
    '''
 
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(2)
    root.right.left.left = Node(3)
    root.right.left.right = Node(4)
 
    sinkNodes(root)
    inorder(root)
