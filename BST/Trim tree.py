# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        def trim(node):
            if not node:
                return None
            elif node.val > high:
                return trim(node.left)
            elif node.val < low:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)
    def printInorder(self,root): 
        if root: 
            # First recur on left child 
            self.printInorder(root.left) 
            # then print the data of node 
            print(root.val), 
            # now recur on right child 
            self.printInorder(root.right) 
root = TreeNode(3)
root.right=TreeNode(4)
root.left = TreeNode(0)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(1)
r=Solution()
root= r.trimBST(root,1,3)
r.printInorder(root)
