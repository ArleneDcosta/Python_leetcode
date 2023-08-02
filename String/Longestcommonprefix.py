def solve(l):
    l.sort(key=len)
    minval = l[0]
    l.pop(0)
    i=len(minval)
    while(i>=0):
        flag=1
        for ele in l:
            if not ele.startswith(minval[0:i]):
                flag=0
                break
        if flag==1:
            return minval[0:i]
                
        i-=1
    return ""   
        
        
        
print solve(["dog","racecar","car"])
