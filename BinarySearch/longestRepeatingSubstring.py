def longestRepeatingSubstringbf(S):
    substr_set = set()
    n = len(S)
    ans = 0

    for i in range(n):
        for j in range(i+1,n+1):
            substr = S[i:j]
            if substr not in substr_set:
                substr_set.add(substr)
            else:
                ans = max(ans,len(substr))
    return ans

def longestRepeatingSubstringbs(S):
    def findRepeatingSubstring(length):
        #easiest way would we a sliding window
        seen =  set()
        '''
        for i in range(n - length + 1):
            #Below slice can be adjusted with Sliding window logic
            #Convert letter into a number
            substr = S[i:i+length]
            h = hash(substr)
            if h in seen:
                return True
            seen.add(h)
        '''
        h = 0
        for i in range(length):
            h = h * 26 + nums[i]
        seen.add(h)
        for i in range(1, n-length + 1):
            h  = h * 26 - nums[i - 1] * 26 ** length + nums[i+length-1]
            if h in seen:
                return True

            seen.add(h)
        return False
    nums = [ ord(c) - ord('a') for c in S]
    n = len(S)
    left = 0 #lower bound of repeating Substring
    right = n - 1 #upper bound of repeating Substring. The string itself cannot be so we reduce by 1
    while(left < right):
        mid  = left + (right - left + 1)// 2
        print(right,left,mid)
        if findRepeatingSubstring(mid):
            left = mid
        else:
            right = mid - 1

    return left #because left will be equal to right since while loop



print(longestRepeatingSubstringbs("AreeAr"))

'''
0th:0 * 26 + 1 = 
1st:(0*26 + 1)*26 = 0*26*26 + 26 + 2
2nd: (26*26 + 26 + 2) = 0*26*26*26 + 26*26 + 2*26 + 3
'''