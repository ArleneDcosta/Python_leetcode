import collections as c
def minSteps(s, t):
    count = c.Counter(s)
    print count,c.Counter(t)
    count &= c.Counter(t) # find the intersection between s and t
    print count,list(count.elements())
    ans = len(s) - len(list(count.elements()))
    return ans

print(minSteps('baab','abaa'))
