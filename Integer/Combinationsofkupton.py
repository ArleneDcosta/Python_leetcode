def combine(n, k):
    def backtrack(start, end, tmp):
        if len(tmp) == k:
            result.append(tmp[:])
        else:
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(i+1,end, tmp)
                tmp.pop()
        
    result = []
    nums = [i for i in range(1,n+1)]
    print nums
    backtrack(0, n, [])
    return result
print combine(4,2)
