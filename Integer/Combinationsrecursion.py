def combine(n, k):
    ds=[]
    res=[]
    comSum(1,k,ds,n,res)
    return res

def comSum(ind,k,ds,n,res):
    print(ind,k,ds,n,res)
    if ind==n+1:
        if k==len(ds):
            res.append(ds.copy())
        return
    ds.append(ind)
    comSum(ind+1,k,ds,n,res)
    ds.pop()
    comSum(ind+1,k,ds,n,res)


print(combine(n = 4, k = 2))
