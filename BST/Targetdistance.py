import collections
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.val = data
        self.par = None
        self.left = self.right = None
        
def distanceK(root, target, K):
    def dfs(node, par = None):
        if node:
            node.par = par
            dfs(node.left, node)
            dfs(node.right, node)

    dfs(root)
    queue = collections.deque([(target, 0)])
    seen = {target}
    while queue:
        if queue[0][1] == K:
            return [node.val for node, d in queue]
        node, d = queue.popleft()
        
        for nei in (node.left, node.right, node.par):
            if nei and nei not in seen:
                seen.add(nei)
                queue.append((nei, d+1))
                print nei.val,d+1

    return []

root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.left.right.left = Node(7)
root.left.right.right = Node(4)
root.right.left = Node(0)
root.right.right = Node(8)
print distanceK(root,root.left,2)
