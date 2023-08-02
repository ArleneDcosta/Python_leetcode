def solve(l):
    #l.sort()
    l=[str(x) for x in l]
    for element in l:
        if l.count(element)%2==1:
            return int(element)
            
print solve([4,3,6,2,6,4,2,3,4,3,3])
