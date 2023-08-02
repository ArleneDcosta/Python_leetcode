def get_subsets(nums):
    def backtrack(i,curNums):
        print('Startt',i,curNums)
        ans.append(curNums[:])
        #Cannot use bit manipulation because cannot represent [1,2,2] same number will become 0
        #Is not the same as sublist
        for j in range(i,n):
            if j > i and nums[j] == nums[j-1]:
                continue

            curNums.append(nums[j])
            print(j, curNums)
            backtrack(j+1,curNums)
            print('backtracking popping',j,curNums,nums[j])
            curNums.pop()

    n = len(nums)
    nums.sort()
    ans = []
    backtrack(0,[])

    return ans

if __name__ == '__main__':
    print(get_subsets([1,2,2,3]))