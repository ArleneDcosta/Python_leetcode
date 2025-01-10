from typing import List
from collections import Counter

def checkPalindrome(s):
    i = 0
    j = len(s) - 1
    while(i < j):
        if s[i]!=s[j]:
            return False
        i += 1
        j -= 1
    return True


def countPalindromicSubsequence(s: str) -> int:
    # count =  Counter(s)
    # resarr = [s[0]]
    # res = 0
    # for i in range(1,len(s)):
    #     currlist = []
    #     for str in resarr:
    #         currstr = str + s[i]
    #         if len(currstr) <= 3:
    #             currlist.append(currstr)
    #     if s[i] not in resarr:
    #         resarr.append(s[i])
    #     resarr += currlist
    # resarr = list(set(resarr))
    # for str in resarr:
    #     if len(str) == 3 and checkPalindrome(str):
    #         res += 1
    # return res
    dic = {}
    ans = set()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = [i]
        else:
            dic[s[i]].append(i)
    print(dic)
    for key,indices in dic.items():
        first,last = indices[0],indices[-1]
        mid_chars = set(s[first+1:last])
        for mid in mid_chars:
            ans.add(key+mid+key)
    return len(ans)

if __name__ == '__main__':
    print(countPalindromicSubsequence(s = "aabca"))
    print(countPalindromicSubsequence(s = "bbcbaba"))