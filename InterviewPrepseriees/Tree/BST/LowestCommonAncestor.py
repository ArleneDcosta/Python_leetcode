class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insert(self, root, val: int):
        if not root:
            root = TreeNode(val)
            return root

        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
        return root

    def printinorder(self,root):
        # if root:
        #     self.printinorder(root.left)
        #     print(root.val, end=' ')
        #     self.printinorder(root.right)

        if root:
            print(root.val)
        if root.left:
            self.printinorder(root.left)
        if root.right:
            self.printinorder(root.right)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p or root.val == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        print(left,right)
        if left and right:
            return root
        return left if left else right

if __name__ == '__main__':
    root = [6,2,8,0,4,7,9,3,5]
    p = 2
    q = 4
    s = Solution()
    
    rootNode = None
    
    currNode = None
    for num in root:
        rootNode = s.insert(rootNode,num)

    
    #print(s.printinorder(rootNode))
    
    print(s.lowestCommonAncestor(rootNode,p,q).val)