class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def rotateRight(self,head, k):
        if not head:
            return head
        tem=self.glist(head)
        for i in range(k%len(tem)):  
            tem.insert(0,tem.pop())
        return self.gnode(tem)
    
    def glist(self,node): 
        re=[]
        while node.next:
            re.append(node.val)
            node=node.next   
        re.append(node.val)
        return re
    
    def gnode(self,l):
        p=head=ListNode()
        for i in l:
            p.next=ListNode(i,None)
            p=p.next
        return head.next

object = Solution()
o = head=ListNode(1,None)
for i in [2,3,4,5]:
    o.next = ListNode(i,None)
    o = o.next
node = object.rotateRight(head,2)
while node is not None:
    print(node.val)
    node = node.next
