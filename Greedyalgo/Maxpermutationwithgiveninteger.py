def solve(A,B):
    i = 0
    _max = len(A)
    d = { x:i for i,x in enumerate(A)}
    print(d)

    while B and i< len(A):
        j = d[_max]
        if i == j:
            pass
        else:
            B-=1
            A[i],A[j] = A[j],A[i]
            d[A[i]],d[A[j]] = d[A[j]],d[A[i]]

        i+=1
        _max-=1
        #value minus the current max value i.e 4 then 3

solve([1,2,3,4],1)
            
    
