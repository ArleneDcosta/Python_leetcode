def solve(s,k):
    count = 0
    set1 = list(set(list(s)))
    l = list(s)
    for char in set1:
        if l.count(char)==1:
            print char
            count+=1
        if count == k:
            return
    return
solve("ABCDBAGHCHFAC",3)
