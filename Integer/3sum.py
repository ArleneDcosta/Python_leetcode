'''Unique triplets that add up to 0'''

def solve(nums):
    res=[]
    nums.sort()
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r-=1
            elif threeSum < 0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])

                while(nums[l] == nums[l + 1] and l< r):
                    l += 1
                while (nums[r] == nums[r - 1] and l < r):
                    r -= 1
                l += 1
                r -= 1
    return res


def solve_bruteforce(nums):
    res = []
    nums.sort()  # Sorting the array to handle duplicates more easily

    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements for the first element

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicate elements for the second element

            for k in range(j + 1, n):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue  # Skip duplicate elements for the third element

                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])

    return res
if __name__ == '__main__':
    print(solve([-2,-2,0,0,2,2]))
    print(solve([-1,2,1,-4,0]))
 
