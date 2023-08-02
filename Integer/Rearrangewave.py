def solve(l):
    l.sort()
    for i in range(1,len(l)):
        if i+1<len(l) and i%2!=0:
            l[i],l[i+1] = l[i+1],l[i]
    print l

solve([1,2,3,4,5,5,6,7,8])
        
    
