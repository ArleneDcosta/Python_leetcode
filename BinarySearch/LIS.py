def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    print(tails)
    #i = left ,j = right
    for x in nums:
        i, j = 0, size
        while i != j:
            #min value will be in front side hence right is assigned [first occurrence will be required]
            m = (i + j) // 2
            print(m,i,j)
            if x < tails[m]:
                #right = mid
                j = m

            else:
                #left = mid + 1
                i = m + 1
        tails[i] = x
        print(tails)
        size = max(i + 1, size)
    return size


if __name__ == '__main__':
    print(lengthOfLIS([1,2,9,6,7]))