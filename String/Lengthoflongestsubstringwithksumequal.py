def checkpalindrome(s):
    print s
    sumF=0
    sumS=0
    if len(s)%2!=0:
        return 0
    else:
        for i in range(0,len(s)/2):
            sumF+=int(s[i])
        for i in range(len(s)/2,len(s)):
            sumS+=int(s[i])
        if sumF == sumS:
            return 1
        else:
            return 0
    
def solve(s):
    s = list(s)
    result=[]
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)+1):
            if checkpalindrome(s[i:j]):
                result.append("".join(s[i:j]))
    
    print result

solve('123123')
    
    
