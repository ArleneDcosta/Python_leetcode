def getNoZeroIntegers(n):
    for num in range(1, n):
        if '0' not in ''.join([str(num), str(n - num)]):
            return [num, n - num]


print getNoZeroIntegers(2)
