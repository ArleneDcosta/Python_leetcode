#Same to max disjoint intervals
def solve(l):
    l.sort(key = lambda x:x[1])

    prev_e = l[0]
    count = 1
    for s,e in l:
        if s > prev_e:
            count+=1
            prev_e = s,e

    return count
