from typing import List

def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    start = 0
    end = 1
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1
    else:
        countdict = {}
        countdict[s[0]] = 1
        while( end < len(s) and start <= end):
            if s[end] in countdict:
                countdict[s[start]] -= 1
                if countdict[s[start]] == 0:
                    del countdict[s[start]]
                start += 1
            else:
                countdict[s[end]] = 1
                end += 1
            res = max(res, (end-start))
        return res

if __name__ == '__main__':
    print(lengthOfLongestSubstring("abcabcbb"))
    print(lengthOfLongestSubstring("bbbbb"))
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("arlene"))