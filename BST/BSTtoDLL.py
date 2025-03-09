class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BSTtoDLL:
    def __init__(self):
        self.head = None  
        self.prev = None  

    def bst_to_dll(self, root):
        if not root:
            return None

        self.bst_to_dll(root.left)

        dll_node = DLLNode(root.val)

        if self.prev is None:
            self.head = dll_node
        else:
            self.prev.next = dll_node
            dll_node.prev = self.prev

        self.prev = dll_node

        self.bst_to_dll(root.right)

        return self.head  

def print_dll(head):
    current = head
    while current:
        print(current.val, end=" <-> " if current.next else "")
        current = current.next
    print()

if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(5)

    converter = BSTtoDLL()
    dll_head = converter.bst_to_dll(root)
    print_dll(dll_head)
