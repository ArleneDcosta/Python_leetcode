def majorityElement(A):
    n = len(A)
    ans = 0
    for b in range(0,32):
        ones = 0
        for num in A:
            if (1<<b) & num:
                ones+=1
        print(num,ones,b)
        if ones > n//2:
            ans += ( 1 << b)
    return ans


print(majorityElement([1,1,1,1,2,2,3,3,3]))
# print(1<<0)
# print(1<<1)
# print(2^2)

