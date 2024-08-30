def findTheLongestVowelEvenSubstring(s):
    n = len(s)
    dp = {0:-1}
    ans = 0
    parity = 0
    vowels = "aeiou"

    for i,c in enumerate(s):
        if c in vowels:
            index = vowels.index(c)
            parity ^= (1<<index)
        print("Before", dp, parity, i,c)
        if parity in dp:
            ans = max(ans,i-dp[parity])
        else:
            dp[parity] = i
        print("After dp", dp,'parity',parity,'i',i,'ans',ans)
    return ans

if __name__ == '__main__':
    #Containing even substrings
    print(findTheLongestVowelEvenSubstring("aa"))
# k = 8
# k ^= (1<<3)
# print(k)
#print(1<<1)