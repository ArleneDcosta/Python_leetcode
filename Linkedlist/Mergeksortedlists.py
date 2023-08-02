class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    res = defaultdict(int) # Preallocate an array
    tracker = output = ListNode() # initialize a tracker and an output, which are the same linked list
    for l in lists: # go through all lists, and add how many of each number you find to our dict
        traversal = l
        if traversal:
            while traversal.next:
                res[traversal.val] += 1
                traversal = traversal.next
            res[traversal.val] += 1
    for key in sorted(res.keys()): # go through our keys in order, adding them to output
        if res[key] == 0:
            continue
        for _ in range(res[key]):
            tracker.next = ListNode(key)
            tracker = tracker.next
    return output.next
