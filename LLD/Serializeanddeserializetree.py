class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def inorder(root):
            curstr = ""
            if root is not None:
                curstr += inorder(root.left)
                curstr = str(root.val) + "," + curstr + ","
                curstr += inorder(root.right)
                return curstr
            else:
                return "N"
        serstr = inorder(root)
        return serstr

    def deserialize(self, data):
        root = None
        data = data.split(",")
        def helper():
            if not data:
                return None
            
            val = data.pop(0)
            if val == 'N':  # Null node
                return None
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()


def inorderfunc(root):
    if root is not None:
        print(root.val)
        if root.left:
            inorderfunc(root.left)
        
        if root.right:
            inorderfunc(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))



print(ser.serialize(root))
print(inorderfunc(ans))