def solve(w):
    d={}
    res=0
    for ele in w:
        if ele in d:
            d[ele]+=1
        else:
            d[ele]=1

    for ele in d:
        if d[ele]%2!=0:
            res+=1

    return res

print solve("acbcbba")
print solve("axxaxa")
print solve("aaaa")
