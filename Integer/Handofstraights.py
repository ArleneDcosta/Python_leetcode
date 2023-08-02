import collections
def solve(hand,W):
    count = collections.Counter(hand)
    print 'Count',count
    while count:
        m = min(count)
        print 'm',m
        for k in xrange(m, m+W):
            v = count[k]
            print 'v',v,'m+W',m+W
            if not v: return False
            if v == 1:
                del count[k]
            else:
                count[k] = v - 1

    return True
  


print solve([1,2,3,6,2,3,4,7,8],3)
    
'''[1,2,3],[2,3,4],[6,7,8]'''
