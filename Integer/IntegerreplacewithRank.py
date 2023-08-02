def solve(l):
    t = list(set(l))
    t.sort()
    result = []
    for i in l:
        result.append(t.index(i)+1)
    print result
solve([10,8,15,12,6,20,1])
