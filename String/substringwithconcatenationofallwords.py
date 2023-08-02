from collections import Counter
def findSubstring(s,words):
    result = []
    origin, M, N = Counter(words), len(words[0]), len(s)
    print('Count of words',origin)
    print('Len of first word',len(words[0]))
    print('Len of string',len(s))
    L = len(words)
    print('Len of words',len(words))
    for i in range( N - M*L  + 1):
        current = Counter(origin)
        flag = True
        for j in range(i, i + M*L, M):
            if not current[s[j:j+M]]: 
                flag = False
                break
            else:
                current[s[j:j+M]] -= 1
        print current
        if flag : result.append(i)
    return result

print findSubstring("barfoofoobarthefoobarman",["bar","foo","the"])
