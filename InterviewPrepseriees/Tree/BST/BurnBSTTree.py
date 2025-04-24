
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def insert(self):
        root = TreeNode(1)
        root.left = TreeNode(5)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(9)
        root.left.right.right = TreeNode(2)

        root.right.left = TreeNode(10)
        root.right.right = TreeNode(6)
        return root
        # if not root:
        #     root = TreeNode(val)
        #     return root

        # curr = root
        # while True:
        #     if val < curr.val:
        #         if curr.left:
        #             curr = curr.left
        #         else:
        #             curr.left = TreeNode(val)
        #             break
        #     else:
        #         if curr.right:
        #             curr = curr.right
        #         else:
        #             curr.right = TreeNode(val)
        #             break
        # return root
    
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
    
    def total_time_for_infection(self,root,start):
        g = defaultdict(list)
        minute = -1
        def create_graph(root):
            if root is not None:
                if root.left is not None:
                    g[root.val].append(root.left.val)
                    g[root.left.val].append(root.val)
                    create_graph(root.left)
                if root.right is not None:
                    print(root.right.val)
                    g[root.val].append(root.right.val)
                    g[root.right.val].append(root.val)
                    create_graph(root.right)
        create_graph(root)
        queue = [[start]]
        visited = set()
        visited.add(start)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in g[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            minute += 1
        return minute

if __name__ == '__main__':
    # root = [1,5,3,None,4,10,6,9,2]
    # start = 3

    # rootval = None
    b = BST()
    root = b.insert()

    print(b.total_time_for_infection(root,3))
    