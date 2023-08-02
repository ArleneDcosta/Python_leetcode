def solve(l):
    result = []
    for i in range(0,len(l)):
        max = -1
        for ele in sorted(l[i+1:]):
            if ele > l[i] and ele > max:
                max = ele
                break
        result.append(max)
                
    return result
        
        
        
print solve([10,100,93,32,35,65,80,90,94,6])
