from collections import Counter
from functools import lru_cache

def numberOfGoodSubsets(nums):
    primes = []
    for num in range(2,31):
        isPrime = True
        i = 2

        while i*i <= num:
            if num % i == 0:
                isPrime = False
                break
            i+=1
        if isPrime:
            primes.append(num)
    print(primes)
    count = Counter(nums)
    keys = list(count.keys())
    n = len(count)
    print(n,count)
    @lru_cache(None)
    def dp(i,mask):
        print('i',i,'mask',mask)
        if i == n:
            return 1
        num = keys[i]

        #not pick current number
        ans = dp(i+1,mask)
        print('not picked num',num,'i',i,'ans',ans)
        #pick current number
        if num!= 1:
            primeMask = sum( 1<<i for i,p in enumerate(primes) if num % p == 0)
            if num%4 != 0 and num % 9 != 0 and num %25 != 0 and mask & primeMask == 0:
                ans += dp(i+1, mask | primeMask) * count[num]
        print('picked', i, ans)
        return ans
    mod = 10**9 + 7
    return ((dp(0,0) - 1) * pow(2,count[1],mod)) % mod #To remove the empty subset and if 1 is more than 1


def find_subsets(i, subset, keys, subsets):
    n = len(keys)

    if i == n:
        subsets.append(subset[:])  # Append a copy of the current subset to the list of subsets
        return

    # Not pick the current element
    find_subsets(i + 1, subset, keys, subsets)

    # Pick the current element
    subset.append(keys[i])
    find_subsets(i + 1, subset, keys, subsets)
    subset.pop()  # Backtrack to the previous state by removing the last element


def get_subsets(keys):
    subsets = []
    find_subsets(0, [], keys, subsets)
    return subsets


if __name__ == '__main__':
    print(numberOfGoodSubsets([1,2,3,5]))
    print(get_subsets([1,2,3,5]))
#print(2&3)
