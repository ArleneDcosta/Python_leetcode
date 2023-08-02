def countSubstrings(s):
    res=[]
    for i in range(0,len(s)):
        for j in range(i+1,len(s)+1):
            res.append(s[i:j])
    print res
    count = 0
    for ele in res:
        if ele == ele[::-1]:
            count+=1
    return count


print countSubstrings("abc")
