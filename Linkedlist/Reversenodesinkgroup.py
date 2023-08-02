class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        array = []
        curr = head
        while curr:
            array.append(curr.val)
            curr = curr.next
        
        curr = head
        size = len(array)
        for i in range(k - 1, size, k):
            for j in range(i, i - k, -1):
                curr.val = array[j]
                curr = curr.next
        
        return head
