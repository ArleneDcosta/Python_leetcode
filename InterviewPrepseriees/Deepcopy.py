
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def getIndex(self,node,nodelist):
        for i in range(0,len(nodelist)):
            if nodelist[i] == node:
                return i
        return 0

    def copyRandomList(self, head):
        if head is None: return None
        mapping = {}
        cur = head
        while cur:
            mapping[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                mapping[cur].next = mapping[cur.next]
            if cur.random:
                mapping[cur].random = mapping[cur.random]
            cur = cur.next
        return mapping[head]

if __name__ == '__main__':

    firstnode = Node(7)
    secondnode = Node(13)
    thirdnode = Node(11)
    fourthnode = Node(10)
    fifthnode = Node(1)
    firstnode.next = secondnode
    secondnode.next = thirdnode
    thirdnode.next = fourthnode
    fourthnode.next = fifthnode
    fifthnode.next = None
    secondnode.random = firstnode
    thirdnode.random = fourthnode
    fourthnode.random = secondnode
    fifthnode.random = firstnode
    currnode = firstnode

    obj = Solution()
    res = obj.copyRandomList(firstnode)
    while(res != None):
        print(res.val)
        res = res.next
