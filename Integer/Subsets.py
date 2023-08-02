def subsets(nums):
    def backtrack(first = 0, curr = []):
        # if the combination is done
        if len(curr) == k:  
            output.append(curr[:])
            print(k,output)
            return
        for i in range(first, n):
            # add nums[i] into the current combination
            curr.append(nums[i])
            # use next integers to complete the combination
            backtrack(i + 1, curr)
            # backtrack
            curr.pop()
        
    output = []
    n = len(nums)
    for k in range(n + 1):
        print("K",k)
        backtrack()
    return output


print(subsets([1,2,3]))
