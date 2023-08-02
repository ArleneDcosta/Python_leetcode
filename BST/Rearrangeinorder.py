class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def inorder(root, retNodeList):
    if root is None:
        return
        
    if root.left is not None:
        inorder(root.left, retNodeList)
        
    retNodeList[0].right = TreeNode(val=root.val)
    retNodeList[0] = retNodeList[0].right
        
    if root.right is not None:
        inorder(root.right, retNodeList)
        
def increasingBST(root):
    t = TreeNode()
    retNodeList = [t]
    inorder(root, retNodeList)
    return t.right

root = TreeNode(5)
root.left = TreeNode(3)
root.right =  TreeNode(6)
root.left.left =  TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)
root.left.left.left = TreeNode(1)
root.right.right.left = TreeNode(7)
root.right.right.right = TreeNode(9)
l = increasingBST(root)
while(l is not None):
    print (l.val)
    l=l.right

