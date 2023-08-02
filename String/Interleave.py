def isInterleave(s1,s2,s3):
    if len(s1) + len(s2) != len(s3):
            return False
        @cache
        def dfs(i, j):
            if i == len(s1) and j == len(s2):
                return True
            choose_s1, choose_s2 = False, False
            if i < len(s1) and s1[i] == s3[i + j]:
                choose_s1 = dfs(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                choose_s2 = dfs(i, j + 1)

            return choose_s1 or choose_s2

        return dfs(0, 0)

print(isInterleave(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"))   
    
