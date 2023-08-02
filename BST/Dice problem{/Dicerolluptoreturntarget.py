def dp(d, f, target):
    A = [[0] * (target + 1) for _ in range(d + 1)]
    print A
    A[0][0] = 1
    for i in range(1, d + 1):
        for j in range(i, target + 1):
            for k in range(1, f + 1):
                if j - k >= 0:
                    A[i][j] += A[i - 1][j - k]
    return A[-1][-1]% (10 ** 9 + 7)
   


print dp(2,6,7)
