from typing import List
from collections import Counter

def minimumIndexUnderstand(nums):
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        def most_frequent(data):
            # Create Counter object, which is a dictionary subclass for counting hashable objects.
            counter = Counter(data)
            
            # Initialize max_count and max_item
            max_count = -1
            max_item = None

            # Iterate over dictionary items
            for item, count in counter.items():
                # Update max_item and max_count if a higher count is found
                if count > max_count:
                    max_count = count
                    max_item = item

            return max_item, max_count
        

        dom, cnt = most_frequent(nums) # returns dominant number and it's count
        left, right = 0, cnt
        for i in range(n):
            if nums[i] == dom:
                left += 1
                right -= 1
            if left * 2 > i + 1 and right * 2 > n - (i + 1):
                return i
        
        return -1

def minimumIndexOptimized(nums):
    dom, cnt = max(Counter(nums).items(), key = lambda x: x[1])
    left, cut = 0, 2*cnt - len(nums)
    print(cnt,cut)
    if cut < 2: 
        return -1

    for i, num in enumerate(nums):

        left+= 2*(num == dom)
        print('left',left)
        if 1 < left - i <= cut: 
            return i

def minimumIndex(nums: List[int]) -> int:
    def helper(mid):
        lefthalf = nums[0:mid+1]
        righthalf = nums[mid+1:]
        leftcount = Counter(lefthalf)
        rightcount = Counter(righthalf)
        maxleftkey,maxrightkey,leftval,rightval = -1,-1,-1,-1
        for key,val in leftcount.items():
            if val >= leftval:
                maxleftkey = key
                leftval = val

        for key,val in rightcount.items():
            if val >= rightval:
                maxrightkey = key
                rightval = val
        print(righthalf)
        if maxrightkey == maxleftkey and len(lefthalf) < 2 * leftcount[maxleftkey] and len(righthalf) < 2 * rightcount[maxrightkey]:
            return True
        return False

    totalcount = Counter(nums)
    maxval = 0
    maxkey = -1
    for key,val in totalcount.items():
        if val >= maxval:
            maxkey = key
            maxval = max(val,maxval)

    for i in range(0,len(nums)):

        if nums[i] == maxkey and helper(i):
            return i

    return -1

if __name__ == '__main__':
    nums = [1,2,2,2]
    print(minimumIndexOptimized(nums))

    nums = [2,1,3,1,1,1,7,1,2,1]
    print(minimumIndexOptimized(nums))

    nums = [3,3,3,3,7,2]
    print(minimumIndexOptimized(nums))