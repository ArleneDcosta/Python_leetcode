def solve(l):
    result=[]
    for i in range(0,len(l)):
        result.append(sum(l[0:i+1]))
    return result


print solve([1,2,3,4])
