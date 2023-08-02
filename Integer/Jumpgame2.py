import sys
def jump(nums):
    
    N = len(nums)
    
    jump_count = [sys.maxsize] * N
    
    for i in range(N):
        if i == 0:
            jump_count[i] = 0
            
        for j in range(1, nums[i] + 1):
            print(i,j),jump_count
            if i + j >= N:
                break
            jump_count[i + j] = min(jump_count[i] + 1, jump_count[i + j])
            
    return jump_count[N - 1]


print jump([2,3,1,1,4])
