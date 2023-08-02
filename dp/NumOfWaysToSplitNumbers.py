def numOfCombinations(num):
    n = len(num)
    #dp = [[0]* (n + 1) for _ in range(n+1)]# dp[i][l] = the total ways to split the string
    # with last number ending at i and the length of the last number is l
    preSum = [[0] * (n + 1) for _ in range(n + 1)]  # dp[i][l] = the total ways to split the string
    # with last number ending at i and the length of the last number is 1...l
    #Understand the below code with example: https://www.youtube.com/watch?v=xe6mfpv1JFA&t=123s
    # lcs = [[0] * (n + 1) for _ in range(n + 1)]
    # for i in range(n-2,-1,-1):
    #     for j in range(i+1,n):
    #         #here i will be on left and j will be on right
    #         if num[i] == num[j]:
    #             lcs[i][j] = 1 + lcs[i+1][j+1]
    #         else:
    #             lcs[i][j] = 0
    # print(lcs)
    for i in range(n):
        for l in range(1,i+2):
            # As your length is 0 based i.e when i =4 then your length will be 5
            #l is also the length of preceding comma number
            j = i - l + 1 #j =  start of the last number
            if num[j] == '0':
                #dp[i][l] = 0
                curr = 0
            elif j == 0:
                # 4 - 5
                #dp[i][l] = 1 #base case
                curr = 1
            else:
                maxL2 = 0
                if j < l:# if remaining string is less than current length
                    maxL2 = j
                #else:
                    #Here j-1 is start string and j is end string
                    # c1 = lcs[j-l][j]
                    # if c1 >=l or num[j-l+c1]<=num[j+c1]:
                    #     maxL2 = l
                    # else:
                    #     maxL2 = l - 1
                elif num[j-l:j] <= num[j:i+1]: #equal
                    maxL2 = l
                else:
                    #25423
                    maxL2 = l - 1
                #Not optimized
                # for l2 in range(1,maxL2+1):
                #     dp[i][l] += dp[j-1][l2]

                #dp[i][l] = preSum[j-1][maxL2]
                curr = preSum[j - 1][maxL2]
            preSum[i][l] = preSum[i][l-1] + curr
    mod = 10**9 + 7

    #print(dp)
    print(preSum)
    return preSum[n-1][n] % mod


print(numOfCombinations("0123"))