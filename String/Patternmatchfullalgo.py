#video:https://www.youtube.com/watch?v=HAA8mgxlov8
def isMatch(s,p):
    # TOP-Down Memoization
    cache = {}
    def dfs(i,j):
        if (i,j) in cache:
            return cache[(i,j)]
        if i>=len(s) and j >= len(p):
            #if i is outofBounds and j is outofBounds
            return True
        if j>=len(p):
            #eg i,s=aa and j,p = a
            return False
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        # 1 character is never going to be a *
        if (j+1)< len(p) and p[j+1] == "*" :
            cache[(i,j)] = (dfs(i,j+2) or# dont use current char[when 0 case c*a,a]
            (match and dfs(i+1,j)))  #use * (the current character matched)empty
            return cache[(i,j)]
        if match:
            cache[(i,j)] = dfs(i+1,j+1)
            return cache[(i,j)]
        cache[(i,j)] = False
        #eg ab*ab*
        return False
    return dfs(0,0)
print isMatch('aa','a*')
