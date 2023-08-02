from functools import lru_cache

def minTheDifference(mat,target):
    @lru_cache(None)
    def dp(row,ssum):
        if row == m:
            return abs(ssum - target)
        ans = 1000000
        for num in mat[row]:
            ans = min(ans,dp(row+1,num+ssum))
            if num + ssum >= target:
                break
        return ans
    m = len(mat)

    #remove the duplicates
    for i in range(m):
        mat[i] = sorted(set(mat[i]))
    return dp(0,0)

print(minTheDifference([[1,0,0],[0,0,0],[7,8,9]],15))
# 1 0 0
# 0 0 0
# 7 8 9