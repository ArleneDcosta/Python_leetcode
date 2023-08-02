def maxDotProduct(A, B):
    A_len ,B_len = len(A),len(B)
    dp = [ [0]*B_len for i in range(A_len)]
    for i in range(0,A_len):  
        for j in range(0,B_len): 
            #Find current dot product value
            dp[i][j] = A[i] * B[j]
                
            #Case when we are taking both index(i,j) in A and B
            #Taking max with 0 to make sure the previous number is not negative
            if (i > 0 and j > 0):
                dp[i][j] += max(0, dp[i-1][j-1])
                
                
            #Case when we are not taking the index(i) in A, comparing with curr value
            if (i > 0):
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                
                
            #// Case when we are not taking the index(j) in B, comparing with curr value
            if (j > 0):
                dp[i][j] = Math.max(dp[i][j], dp[i][j-1])
               
    return dp[A_len-1][B_len-1]


print maxDotProduct
