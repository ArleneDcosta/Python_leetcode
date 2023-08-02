def solve(A,B):
    sortedA = sorted(A)
    sortedB = sorted(B)

    assigned = {b: [] for b in B}
    remaining = []
    print assigned
    print sortedA
    print sortedB
        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
    j = 0
    for a in sortedA:
        if a > sortedB[j]:
            print j,
            assigned[sortedB[j]].append(a)
            print assigned
            j += 1
            
        else:
            remaining.append(a)
    print remaining

        # Reconstruct the answer from annotations (assigned, remaining)
    return [assigned[b].pop() if assigned[b] else remaining.pop()for b in B]
    
#print solve([2,7,11,15],[1,10,4,11])
#print solve([12,24,8,32],[13,25,32,11])
print solve([1,2,3,4],[5,6,7,8])
