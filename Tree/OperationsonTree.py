from typing import List

class Node:
    def __init__(self,val):
        self.val = val
        self.children = [] #no need of left and right as multiple children can be present

class LockingTree:

    def __init__(self, parent: List[int]):
        n = len(parent)
        self.locks = [0] * len(parent)
        self.parent = parent
        self.nodes = {} #key is the node index and value is the node
        self.nodes[0] = Node(0)
        for i in range(1,n):
            val = i
            p = parent[i]
            #check if parent node has been created
            if p not in self.nodes:
                self.nodes[p] = Node(p)
            parentNode =  self.nodes[p]
            if val not in self.nodes:
                self.nodes[val] = Node(val)
            parentNode.children.append(self.nodes[val])

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] > 0:
            return False
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == 0 or self.locks[num] != user:
            return False
        self.locks[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locks[num] > 0:
            return False

        #CHeck if no locked ancestor is present
        par =  num
        hasAncestorLocked = False
        while self.parent[par]!= -1 :
            par = self.parent[par]
            if self.locks[par] > 0:
                hasAncestorLocked = True
                break
        if hasAncestorLocked:
            return False
        #Check descendents
        curNode = self.nodes[num]
        # Check if atleast one child is locked(locked descendent) using Iterative dfs
        stack = [node for node in curNode.children]
        hasLockedDesc = False
        while stack:
            cur = stack.pop()
            if self.locks[cur.val] > 0:
                hasLockedDesc = True
                break
            stack.extend(cur.children)
        if not hasLockedDesc:
            return False
        #perform update
        self.locks[num] = user
        #unlock all descendents
        stack = [node for node in curNode.children]

        while stack:
            cur = stack.pop()
            self.locks[cur.val] = 0

            stack.extend(cur.children)
        return True

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)