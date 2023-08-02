def solve(arr,k,x):
    '''if x<1:
        index = 0
    else:
        index = arr.index(x)
    res=[]
    res.append(arr[index])
    t=1
    s=index-1
    b=index+1
    while len(res)!=k:
        print t,s,b
        if t:
            if(s>-1):
                res.append(arr[s])
                s=s-1
            t=0
        else:
            if b<len(arr):
                res.append(arr[b])
                b=b+1 
            t=1
    res.sort()
    return res'''
    print(sorted(arr, key = lambda y : y - x)[:k])
    return sorted((sorted(arr, key = lambda y : abs(y - x))[:k]))
print(solve([1,2,3,4,5],4,3))
print(solve([1,2,3,4,5],4,-1))       
    
