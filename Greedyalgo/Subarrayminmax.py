ans = 10000000

def subminmax(a,k):
    print(solve(a,len(a),k,0,0,0))
def solve(a, n, k, index, sum, maxsum):
    global ans
     
    # K=1 is the base Case
    if (k == 1):
        maxsum = max(maxsum, sum)
        sum = 0
        for i in range(index,n):
            sum += a[i]
 
        # we update maxsum
        maxsum = max(maxsum, sum)
         
        # the answer is stored in ans
        ans = min(ans, maxsum)
        return 
 
    sum = 0
     
    # using for loop to divide the array into
    # K-subarray
    for i in range(index, n):
        sum += a[i]
         
        # for each subarray we calculate sum ans update
        # maxsum
        maxsum = max(maxsum, sum)
        print(a, n, k - 1, i + 1, sum, maxsum)
        # calling function again
        index,i,solve(a, n, k - 1, i + 1, sum, maxsum)


print(subminmax([2,3,1,1],2))   
print(ans)
