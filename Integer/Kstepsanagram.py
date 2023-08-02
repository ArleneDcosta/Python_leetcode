import itertools
def kSimilarity(A, B):
    if A == B: return 0

    N = len(A)
    alphabet = 'abcdef'
    pairs = [(a, b) for a in alphabet for b in alphabet if a != b]
    index = {p: i for i, p in enumerate(pairs)}
    print len(index)

    count = [0] * len(index)
    for a, b in itertools.izip(A, B):
        if a != b:
            count[index[a, b]] += 1
    print count

    seen = set()
    for size in xrange(2, len(alphabet) + 1):
        for cand in itertools.permutations(alphabet, size):
            i = cand.index(min(cand))
            #min(a,b) here min is 0
            #print i,cand,cand[i:],cand[:i]
            #add sorted ('a','b')it just sorts it
            seen.add(cand[i:] + cand[:i])
    possibles = []
    for cand in seen:
        row = [0] * len(alphabet) * (len(alphabet) - 1)
        for a, b in itertools.izip(cand, cand[1:] + cand[:1]):
            row[index[a, b]] += 1
        #Sprint row
        possibles.append(row)
    
    #print possibles
    ZERO = tuple([0] * len(row))
    memo = {ZERO: 0}
    def solve(count):
        print 'ins'
        if count in memo:
            print count,'inside',memo
            return memo[count]
        
        ans = float('-inf')
        for row in possibles:
            count2  = list(count)
            #all zeroes satisfy the cond that is passed as input
            for i, x in enumerate(row):
                if count2[i] >= x:
                    #print count2,i,x
                    #2 ('b', 'c', 'a') ('a',) ('b', 'c')
                    count2[i] -= x
                else: break
            else:
                ans = max(ans, 1 + solve(tuple(count2)))

        memo[count] = ans
        #original count
        return ans

    return sum(count) - solve(tuple(count))

print kSimilarity("abc","bca")       
