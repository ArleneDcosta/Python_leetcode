# Python implementation of the above approach

# Function to find the length of the
# longest LCS
def maxLengthRepeatedArray(nums1,nums2):
    def helper(length):
        # len =  2 , 10,100 and 0,200 will result in same value when hashBase is 10 so chances of collision is more
        hashSet1 = set()
        hashSet2 = set()
        base  =  101
        mod = 2**32
        a = pow(base,length,mod)
        currHash = 0
        for i in range(m):
            currHash = currHash * base + nums1[i]

            if i >= length:
                currHash -= nums1[i-length] * a

            currHash %= mod
            if i >= length - 1:
                hashSet1.add(currHash)
        currHash = 0
        for i in range(n):
            currHash = currHash * base + nums2[i]

            if i >= length:
                currHash -= nums2[i-length] * a

            currHash %= mod
            if i >= length - 1:
                hashSet2.add(currHash)

        return len(hashSet1.intersection(hashSet2)) > 0



    m = len(nums1)
    n = len(nums2)
    l = 0
    r = min(m,n) #common elements will be smallest from 2 of them
    while(l < r):
        mid =  l + (r - l + 1)//2
        print(mid)
        #Biased towards right
        if helper(mid):
            l = mid
        else:
            r = mid - 1

    return l

if __name__ == '__main__':
    # Driver Code
    nums1 = [1,2,3,2,1]
    nums2 = [3,2,1,4,7]

    # Function call
    print(maxLengthRepeatedArray(nums1,nums2))

# This code is contributed by avanitrachhadiya2155
