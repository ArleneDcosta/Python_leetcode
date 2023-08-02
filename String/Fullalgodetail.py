#video:https://www.youtube.com/watch?v=HAA8mgxlov8
def isMatch(s,p):
    cache = {}
    def helper(i, j):
        if (i,j) in cache:
            return cache[(i,j)]
        if i == len(s) and j == len(p): return True
        if i == len(s): 
            if p[j] == '*':
                cache[(i,j)] = helper(i, j + 1) 
            #check for a* and aa case    
            else:
                cache[(i,j)] = False
            return cache[(i,j)]
        if j == len(p):
            cache[(i,j)] = False
            return cache[(i,j)]
        if p[j] == '?': 
            cache[(i,j)] = helper(i + 1, j + 1)
            return cache[(i,j)]
        if p[j] == '*':
            cache[(i,j)] = helper(i, j + 1) or helper(i + 1, j)
            #best eg is acdcb and *a*b
            return cache[(i,j)]
        if s[i] != p[j]: 
            cache[(i,j)] = False
            return cache[(i,j)]
        cache[(i,j)] = helper(i + 1, j + 1)
        return cache[(i,j)]
    return helper(0, 0)
#print isMatch('adceb','*a*b')
print isMatch('aa','a*')
#print isMatch('cb','?b')
#print isMatch('acdcb','a*c?b')
#print isMatch('aab','c*a*b')
