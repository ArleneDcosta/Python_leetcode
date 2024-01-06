from typing import List

'''
DFS 011110 Remember 
dfs(n) = minimum steps to convert n to 0
helper(n) = minimum steps to convert n to 10000
'''

'''
1 011010 -> 1 100000 -> dfs(1011010) -> 1 + helper(011010) + dfs(100000)
#sxxxxx to 100000[first bit] 
1) if s == 1: dfs(xxxxx)[ convert the remaining to 0] because convert the remaining to 0
2) if s == 0:
2.1 sxxxxx -> s10000 -> 110000 -> dfs(10000)
helper(xxxxx) + 1 + dfs(10000)
'''

'''
# base case[no of operations to convert]
dfs if 0 return 0, if 1 return 1[1st operation]
helper if 0 return 1(01000 to 1000)since you have to convert, if 1 return 0( 10000) [ 2nd operation]
helper
'''
# Time complexity =  O(n) or O(l) here as it is O(V + E)
def minimumOneBitOperations(n: int) -> int:

    def dfs(bits) -> int:
        # Min steps to convert n to 0
        if bits in memo_dfs:
            return memo_dfs[bits]

        #Base case
        if bits == '0':
            return 0
        if bits == '1':
            return 1
        ans  = 0

        if bits[0] == '0':
            ans = dfs(bits[1:])
        else:
            ans = helper(bits[1:]) + 1 + dfs('1' + '0' * (len(bits) - 2))

        memo_dfs[bits] = ans
        return ans

    def helper(bits) -> int:
        # Min steps to convert n to 10000
        if bits in memo_helper:
            return memo_helper[bits]

        #Base case
        if bits == '0':
            return 1
        if bits == '1':
            return 0

        if bits[0] == '1':
            ans = dfs(bits[1:])
        else:
            ans = helper(bits[1:]) + 1 + dfs('1' + '0' * (len(bits) - 2))

        memo_helper[bits] = ans
        return ans

    memo_dfs = {}
    memo_helper = {}

    bits = bin(n)[2:]
    return dfs(bits)

def minimumOneBitOperationsnew(n: int) -> int:
    # ans  = []
    # for i in range( 1 << n):
    #     ans.append(i ^ ( i >> 1))
    ans = 0
    bits =  bin(n)[2:]
    print(bits)
    last_bit = 0
    # Remember the result bit has to be 0
    # According to the above logic of 010 ^ 001 ( graycode logic) to calculate i
    # abcdrf and other will 0abcdr
    for i,bit in enumerate(bits):
        bit = int(bit)
        print(bit)
        if bit == 1:
            cur_bit = last_bit ^ 1
        else:
            cur_bit = last_bit
        ans =  ( ans << 1) + cur_bit
        last_bit = cur_bit
    return ans

if __name__ == '__main__':
    print(minimumOneBitOperationsnew(n=2))

    '''The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.'''

'''Given an integer n, you must transform it into 0 using the following operations any number of times:

Step 1: Change the rightmost (0th) bit in the binary representation of n.
Step 2: Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of opera
110 = 010 = 011 = 001 == 000 
10 = 11 = 01 = 00'''