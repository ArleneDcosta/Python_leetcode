def intersectionSizeTwo(intervals):
    intervals.sort(key = lambda (s, e): (s, -e))
    print intervals
    todo = [2] * len(intervals)
    print todo
    ans = 0
    while intervals:
        (s, e), t = intervals.pop(), todo.pop()
        print (s, e), t,'outer'
        for p in xrange(s, s+t):
            for i, (s0, e0) in enumerate(intervals):
                print i,(s0, e0)
                print todo[i],p,e0
                if todo[i] and p <= e0:
                    todo[i] -= 1
            ans += 1
    return ans

print intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]])
#here 3 is checked with 1,3 and 1,4 and 2,5
#later 4 is checked with 1,3 and 1,4 and 2,5
#1,3 is left with 1
#meaninf 1and4  and 2 and 5 have 2 elements in 3 5
# 1 4 and 2 5 and 3 5 have  [3 4]in common
# later 1 3 have 2 and 3 common
