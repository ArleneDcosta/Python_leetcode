def solve(A):
    l=sorted(A)
    res=[]
    print A
    for ele in A:
        res.append(l.index(ele))
    return res
print solve([8,1,2,2,3])
'''for i in range(0,len(A)):
        if l.index(A[i]) not in res:
            res.append(l.index(A[i]))
        else:
            res.append(res[i-1]+1)
    return res'''
