def smallestNumber(N):
    print( (N % 9 + 1) * pow(10, (N // 9 )) - 1)


if __name__ == '__main__':
    N  = 2
    print(smallestNumber(N))