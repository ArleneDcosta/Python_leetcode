"""
A python program to find distance between n1
and n2 in binary tree
"""
# binary tree node
class Node:
    # Constructor to create new node
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# This function returns pointer to LCA of
# two given values n1 and n2.
def LCA(root, n1, n2):
    
    # Base case
    if root is None:
        return None

    # If either n1 or n2 matches with root's
    # key, report the presence by returning
    # root
    if root.data == n1 or root.data == n2:
        return root
    if root.data == None or root.data == None:
        return None

    # Look for keys in left and right subtrees
    left = LCA(root.left, n1, n2)
    right = LCA(root.right, n1, n2)

    if left is not None and right is not None:
        return root

    # Otherwise check if left subtree or
    # right subtree is LCA
    if left:
        return left
    else:
        return right


# function to find distance of any node
# from root
def findLevel(root, data, d, level):
    
    # Base case when tree is empty
    if root is None:
        return

    # Node is found then append level
    # value to list and return
    if root.data == data:
        d.append(level)
        return

    findLevel(root.left, data, d, level + 1)
    findLevel(root.right, data, d, level + 1)

# function to find distance between two
# nodes in a binary tree
def findDistance(root, n1, n2):
    
    lca = LCA(root, n1, n2)
    print(lca.data)
    # to store distance of n1 from lca
    d1 = []
    
    # to store distance of n2 from lca
    d2 = []
    
    # if lca exist
    if lca:
        
        # distance of n1 from lca
        findLevel(lca, n1, d1, 0)
        
        # distance of n2 from lca
        findLevel(lca, n2, d2, 0)
        print d1,d2,d1[0],d2[0]
        return d1[0] + d2[0]
    else:
        return -1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

#print("Dist(4,5) = ", findDistance(root, 4, 5))
#print("Dist(4,6) = ", findDistance(root, 4, 6))
#print("Dist(3,4) = ", findDistance(root, 3, 4))
print("Dist(2,4) = ", findDistance(root, 2, 4))
#print("Dist(8,5) = ", findDistance(root, 8, 5))

# This article is contributed by Shweta Singh.
