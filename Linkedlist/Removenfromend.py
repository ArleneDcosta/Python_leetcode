# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
    def __init__(self):
        self.n = 0  # initialise global variable to avoid reference before assignment error
    
    def remove(self, node):
        child = None
        # Step 1: Loop to the end of the linked list
        # The code will only proceed if node.next is None, i.e. end of linked list
        if node.next is not None:
            child = self.remove(node.next)
        # Step 2: Check if n = 0, and update current node.next = child if so
        if self.n == 0:
            node.next = child
        # Step 3: Decrement the counter, and check if n was 1 (i.e. n = 0 now)
        # If so, give the node.next instead of the node, since the node will be removed
        self.n -= 1
        return node.next if self.n == 0 else node
        
    def removeNthFromEnd(self, head, n):
        self.n = n  # set global variable
        return self.remove(head)  # get head of updated linked list
