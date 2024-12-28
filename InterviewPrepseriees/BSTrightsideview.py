from typing import List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def gettreeheight(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return 1 + max(gettreeheight(root.left),gettreeheight(root.right))

def getright(root,result):
    if root is None:
        return result
    result.append(root.val)
    if root.right is not None:
        result = getright(root.right,result)
    else:
        result = getright(root.left,result)
    return result

def rightSideView(root):
    if not root:
        return []
    right = rightSideView(root.right)
    left = rightSideView(root.left)
    return [root.val] + right + left[len(right):]

if __name__ == '__main__':
    leftr = TreeNode(5)
    leftroot = TreeNode(2,None,leftr)
    rightr = TreeNode(4)
    rightroot = TreeNode(3,None,rightr)
    root = TreeNode(1,leftroot,rightroot)
    print(rightSideView(root))

    leftr = TreeNode(5)
    leftroot = TreeNode(4, leftr, None)
    leftrootl = TreeNode(2,leftroot,None)
    rightroot = TreeNode(3, None, None)
    root = TreeNode(1, leftrootl, rightroot)
    print(rightSideView(root))

    rightr = TreeNode(4,None,None)
    leftroot = TreeNode(2,None,rightr)
    rightroot = TreeNode(3,None,None)
    root = TreeNode(1,leftroot,rightroot)
    print(rightSideView(root))