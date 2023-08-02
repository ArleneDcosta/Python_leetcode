def solve(n,count):
    if n==0:
        return count
    if n%2==0:
        n = n/2
        count+=1
        return solve(n,count)
    else:
        n = n-1
        count+=1
        return solve(n,count)
print(solve(14,0))
