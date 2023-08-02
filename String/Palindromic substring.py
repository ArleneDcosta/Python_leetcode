def ispalindrome(s):
    i=0
    j=len(s)-1
    while i<=j:
        if s[i]!=s[j]:
            return 0
        i+=1
        j-=1
    return 1
    
def subscheck(s):
    result=[]
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if ispalindrome(s[i:j]):
                result.append(s[i:j])
    result = list(set(result))
    result.sort(key=len)
    return result
print subscheck("google")
