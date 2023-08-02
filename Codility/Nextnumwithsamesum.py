print list(13)

def solve(n):
    l=list(str(n))
    res = list(map(int, l))
    s = sum(res)
    for i in range(n+1,10000):
        temp = list(map(int,list(str(i))))
        if sum(temp)== s:
            return i

    return -1


print solve(28)
print solve(734)
