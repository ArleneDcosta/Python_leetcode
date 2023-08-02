# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    if not head or not head.next:
        return head
        
    node1=head
    node2=head.next
        
    while(True):
        temp = node1.val
        node1.val = node2.val
        node2.val=temp
            
        if(not node2.next or not node2.next.next):
            break            
        node1=node2.next
        node2=node1.next
           
            
    return head

head = Listnode(1)
#head = [1,2,3,4]
