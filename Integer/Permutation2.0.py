def permuteUnique(nums):
    # Purpose: find unique permutations of an array
    # Method: Backtracking
    # Intuition: sort the array, traverse and split, pass duplicates, add the leaf node to path, append path to res.
        
    # init
    res = []
    path = []
        
    # find 
    dfs(nums, path, res)
        
    # return
    return res
    
def dfs(nums, path, res):
    print(f'nums:{nums},papth:{path},res:{res}')
    # add the leaf nodes
    if not nums:
        res.append(path)
        
        # sort the array
    nums.sort()
        
        # traverse and split, pass duplicates, add the leaf node to path
    for i in range(len(nums)):
            
        if i > 0 and nums[i] == nums[i - 1]:
            continue
                
        dfs(nums[:i] + nums[i+1:], path + [nums[i]], res)
def subsetsWithDup(nums):
    # Purpose: find no-duplicate subset of an array
    # Method: backtracking
    # Intuition: sort the array, slice the array, pass duplicates, add to path, append to res
	
    # init
    path = []
    res = []
	
    # find 
    dfs1(nums, path, res)
	
    # return
    return res
	
	
def dfs1(nums, path, res):
    print(f'nums:{nums},path:{path},res:{res}')
    # append to res
    res.append(path)

    # sort the array
    nums.sort()
	
    # slice the array, pass duplicates, add to path
    for i in range(len(nums)):
		
        if i > 0 and nums[i] == nums[i - 1]:
            continue
			
        dfs1(nums[i+1:], path + [nums[i]], res)

print(permuteUnique([1,1,2]))
#print(subsetsWithDup([1,2,3]))
