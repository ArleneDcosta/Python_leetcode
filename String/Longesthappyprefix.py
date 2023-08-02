def longestPrefix(s):
    dp = [0] * len(s)

    for i in range(1, len(s)):
        j = dp[i-1]
        
        while j > 0 and s[j] != s[i]:
            j = dp[j-1]
        if s[j] == s[i]:
            dp[i] = j+1
        print j,i,dp
    return s[len(s)-dp[-1]:]
#longestPrefix("leetcodeleet")
#longestPrefix("level")
print longestPrefix("ababab") 
 
