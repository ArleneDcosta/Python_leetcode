def longestSubarray(nums, limit):

    i, maxq, minq = 0, [], []
        
    for num in nums:
        while len(maxq) and num > maxq[-1]: maxq.pop()
        while len(minq) and num < minq[-1]: minq.pop()
                
        maxq.append(num)
        minq.append(num)
            
        if maxq[0] - minq[0] > limit:
            print nums[i],maxq,minq
            if maxq[0] == nums[i]: maxq.pop(0)
            if minq[0] == nums[i]: minq.pop(0)
            i += 1
            print 'after',nums[i],maxq,minq
                
    return len(nums) - i

print longestSubarray([8,2,4,7],4)
