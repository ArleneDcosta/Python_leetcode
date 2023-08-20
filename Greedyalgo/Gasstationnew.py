def canCompleteCircuit(A,B):
    n = len(A)
    curr = start = 0
    for i,(g,c) in enumerate(zip(A*2,B*2)):
        print(i,(g,c),start,curr,n)
        if i == start + n:
            return start

        curr += (g - c)

        if curr < 0:
            start = i + 0
            curr = 0

print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(canCompleteCircuit([2,3,4],[3,4,3]))
print(canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]))