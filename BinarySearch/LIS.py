def lengthOfLIS(nums):
    tails = [0] * len(nums)
    size = 0
    print(tails)
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) // 2
            print(m,i,j)
            if x < tails[m]:
                j = m

            else:
                i = m + 1
        tails[i] = x
        print(tails)
        size = max(i + 1, size)
    return size


if __name__ == '__main__':
    print(lengthOfLIS([1,2,9,6,7]))