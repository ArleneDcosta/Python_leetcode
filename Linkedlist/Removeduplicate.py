class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # sentinel
    sentinel = ListNode(0, head)

    # predecessor = the last node 
    # before the sublist of duplicates
    pred = sentinel
        
    while head:
        # if it's a beginning of duplicates sublist 
        # skip all duplicates
        
        if head.next and head.val == head.next.val:
            # move till the end of duplicates sublist
            while head.next and head.val == head.next.val:
                head = head.next
            # skip all duplicates
            pred.next = head.next 
        # otherwise, move predecessor
        else:
            pred = pred.next 
                
        # move forward
        head = head.next
            
    return sentinel.next

l = [1,1,2,3,3]
head = ListNode(l[len(l)-1])
for i in range(len(l)-2,-1,-1):
    head = ListNode(l[i],head)
deleteDuplicates(head)
    
    
