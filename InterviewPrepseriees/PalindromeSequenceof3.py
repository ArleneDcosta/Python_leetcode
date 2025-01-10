
def countPalindromicSubsequence(s: str) -> int:
    dic = {}
    ans = set()
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = [i]
        else:
            dic[s[i]].append(i)
    
    for key,indices in dic.items():
        first,last = indices[0],indices[-1]
        mid_chars = set(s[first+1:last])
        for mid in mid_chars:
            ans.add(key+mid+key)
    return len(ans)