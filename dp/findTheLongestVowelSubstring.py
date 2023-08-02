def findTheLongestVowelSubstring(s):
    # rs here parity
    # t = rs - k t = dp[parity], rs is the parity of the current[i] //that was running sum
    n = len(s)
    dp = {0:-1}
    ans = 0
    parity = 0
    vowels = "aeiou"

    for i,c in enumerate(s):
        print("Before", dp, parity,i)
        if c in vowels:
            index = vowels.index(c)

            parity ^= (1<<index)

        if parity in dp:
            ans = max(ans,i-dp[parity])
        else:
            dp[parity] = i
        print("After dp", dp,'parity',parity,'i',i,'ans',ans,'index',index)
    return ans

#Containing even substrings
print(findTheLongestVowelSubstring("ajedfdfdfae"))
# k = 8
# k ^= (1<<3)
# print(k)
#print(1<<1)