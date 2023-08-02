# Python3 program for maximum average sum partition 
MAX = 1000

memo = [[0.0 for i in range(MAX)] for i in range(MAX)] 

# bottom up approach to calculate score 
def score(n, A, k):
    if (memo[n][k] > 0): 
        return memo[n][k] 
    sum = 0
    i = n - 1
    while(i > 0): 
        sum += A[i] 
        memo[n][k] = max(memo[n][k], score(i, A, k - 1) + int(sum / (n - i))) 
        i -= 1
    
    return memo[n][k] 

def largestSumOfAverages(A, K): 
    n = len(A) 
    sum = 0
    for i in range(n): 
        sum += A[i] 

    # storing averages from starting to each i ; 
        memo[i + 1][1] = int(sum / (i + 1))
        print i,i+1,memo[i + 1][1]
    return score(n, A, K) 

# Driver Code 

A = [9, 1, 2, 3, 9] 
K = 3 # atmost partioning size 
print(largestSumOfAverages(A, K)) 
    
# This code is contributed by 
# Surendra_Gangwar 
