# Python implementation of the above approach

# Function to find the length of the
# longest LCS
def maxLengthRepeatedArray(nums1,nums2):
    #n=len(X),#m = len(Y)
    #src taken 0 and 1 and target considered length
    # Create DP table
    n = len(nums1)
    m = len(nums2)
    dp = [[0 for j in range(m + 1)] for i in range(2)]
    print(dp)
    res = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (nums1[i - 1] == nums2[j - 1]):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + 1
                if (dp[i % 2][j] > res):
                    res = dp[i % 2][j]
            else:
                dp[i % 2][j] = 0
            print(i,j,dp)
    return res


# Driver Code
nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]

# Function call
print(maxLengthRepeatedArray(nums1,nums2))

# This code is contributed by avanitrachhadiya2155
