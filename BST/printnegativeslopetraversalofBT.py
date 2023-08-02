# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# Recursive function to perform preorder traversal on the tree and
# fill the dictionary with diagonal elements
def printDiagonal(node, diagonal, dict):
 
    # base case: empty tree
    if node is None:
        return
 
    # insert the current node into the current diagonal
    dict.setdefault(diagonal, []).append(node.data)
    print(dict)
    # recur for the left subtree by increasing diagonal by 1
    printDiagonal(node.left, diagonal + 1, dict)
 
    # recur for the right subtree with the same diagonal
    printDiagonal(node.right, diagonal, dict)
 
 
# Function to print the diagonal elements of a given binary tree
def printDiagonalElements(root):
 
    # create an empty dictionary to store the diagonal element in every slope
    dict = {}
 
    # perform preorder traversal on the tree and fill the dictionary
    printDiagonal(root, 0, dict)
 
    # traverse the dictionary and print diagonal elements
    for i in range(len(dict)):
        print(dict.get(i))
 
 
if __name__ == '__main__':
 
    ''' Construct the following tree
               1
             /   \
            /     \
          2        3
         /        /  \
        /        /    \
       4        5      6
               / \
             /    \
            7      8
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    printDiagonalElements(root)
