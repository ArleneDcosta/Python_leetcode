def maxScore(s):
    res=0
    for i in range(0,len(s)-1):
        count=0
        left = s[0:i+1]
        count+=left.count('0')
        right = s[i+1:]
        count+=right.count('1')
        res = max(count,res)
    return res

print maxScore
