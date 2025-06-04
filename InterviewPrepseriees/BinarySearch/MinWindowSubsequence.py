from collections import defaultdict

def getminwindowsubsequence(S,T):
    if len(S) == len(T) and S == T:
        return S
    elif len(T) >= len(S):
        return ""
    
    def helper(length):
        j = 0
        startindex = 0

        while(startindex < len(S) - length + 1):
            i = startindex
            j = 0
            while(i < startindex + length):
                if S[i] ==  T[j] and j != len(T) - 1:
                    j += 1
                    i += 1
                elif S[i] == T[j] and j == len(T) - 1:
                    j = 0
                    return S[startindex:startindex + length],True
                else:
                    i += 1
            startindex += 1
            
        return "", False

    left = len(T)
    right = len(S)
    finalresult = ""
    while(left < right):
        mid = left + (right - left) // 2
        result,flag = helper(mid)
        if flag:
            right = mid
            finalresult = result
        else:
            left = mid + 1

    return finalresult

def getminwindowsubsequencebf(S,T):
    j = 0
    i = 0

    indexstore  = defaultdict(list)
    for i,char in enumerate(S):
        if char == T[0]:
            indexstore[char].append(i)
        elif char == T[len(T) - 1]:
            indexstore[char].append(i)
    print(indexstore)

    for start in indexstore[T[0]]:
        for end in indexstore[T[len(T)-1]]:
            while( i <= end):
                i = start
                j = 0
                if S[i] ==  T[j] and j != len(T) - 1:
                    j += 1
                    i += 1
                elif S[i] == T[j] and j == len(T) - 1:
                    j = 0
                    return S[start:end+1]
                else:
                    i += 1
        
    return ""

if __name__ == '__main__':
    S = "abcdebddes"
    T = "bde"
    print(getminwindowsubsequence(S,T))

    S = "abbdccdebdde"
    T = "bde"
    print(getminwindowsubsequence(S,T))

    S = "abcabcab"
    T = "aab"
    print(getminwindowsubsequence(S,T))

    S = "abc"
    T = "acb"
    print(getminwindowsubsequence(S,T))

