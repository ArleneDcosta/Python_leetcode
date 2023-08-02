def maxVowels(s, k):
    vowelCount = count = 0
    #print(len(s)-(k-1))
    j = k-1
    vowels = {'a','e','i','o','u'}
    for i in range(k):
        if s[i] in vowels:
            vowelCount += 1
    count = vowelCount
    for i in range(1, len(s)-(k-1)):
        j+=1
        if s[j] in vowels:
            count += 1 
        if s[i-1] in vowels:
            count -= 1
        print 'i ',i,'j ',j,s[j],count,s[j-1]
        if count > vowelCount:
            vowelCount = count
    return vowelCount


print maxVowels('leetcode',3)
