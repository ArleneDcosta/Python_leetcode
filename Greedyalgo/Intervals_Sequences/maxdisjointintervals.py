def solve(l):
    l.sort(key = lambda x:x[1])

    prev_s,prev_e = l[0]
    count = 1
    for s,e in l:
        if s <= prev_e:
            pass
        else:
            count+=1
            prev_s,prev_e = s,e

    return count
