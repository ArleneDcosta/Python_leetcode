'''Unique triplets that add up to 0'''

def solve(nums):
    res=[]
    nums.sort()
    print('Sorted Array is',nums)
    for i,a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue

        l,r = i+1, len(nums)-1
        while l < r:
            print(i,l,r)
            threeSum = a + nums[l] + nums[r]
            print(threeSum)
            if threeSum > 0:
                print('Inside',threeSum)
                r-=1
            elif threeSum < 0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])

                while(nums[l] == nums[l + 1] and l< r):
                    l += 1
                while (nums[r] == nums[r - 1] and l < r):
                    r -= 1
                'Since you have adready traversed the nums[l] element'
                l += 1
                r -= 1
    return res

if __name__ == '__main__':
    print(solve([-2,-2,0,0,2,2]))
    print(solve([-1,2,1,-4,0]))
 
