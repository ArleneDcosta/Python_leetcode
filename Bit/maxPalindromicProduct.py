from typing import List

def maxProduct(s:str) -> int:
    n = len(s)
    #Disjoint palindromes using different indices
    #store valid palindromic subsequences #first index is the length of palindromic string and second is the total bits considereed
    pals = []
    #Trying all combinations good for permutation checks
    for m in range(1,1<<n):
        pal = ""
        for i in range(n):
            #print(m,i,1 << i,m & (1<<i))
            if m & (1<<i) != 0:
                pal += s[i]
        #print(pal)
        if pal == pal[::-1]:
            pals.append((len(pal),m))
    print(pals)
    ans = 0
    for l1,m1 in pals:
        for l2,m2 in pals:
            #Signifies disjoint
            if m1 & m2 == 0:
                ans  = max(ans,l1 * l2)

    return ans
    #Optimization u can do is choose inner for loop if l1 * (n - l1) > ans
    # also if u take a curr mask and use a reversed mask and then u enumerate through it by
    # cur = revsermask ans while(cur): cur = (cur - 1) & reversedmask


if __name__ == '__main__':
    print(maxProduct('accbcaxxcxx'))