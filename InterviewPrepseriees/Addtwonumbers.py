class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, c=0):
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret

if __name__ == '__main__':
    obj = Solution()
    l1 = ListNode(3)
    l1.next = ListNode(4)
    l1.next.next = ListNode(2)
    l2 = ListNode(4)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)
    res = obj.addTwoNumbers(l1,l2)
    while(res != None):
        print(res.val)
        res = res.next