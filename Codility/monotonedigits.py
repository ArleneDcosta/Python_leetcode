print [2,9]*2
def monotoneIncreasingDigits(N):
    digits = []
    A = map(int, str(N))
    print A
    for i in xrange(len(A)):
        for d in xrange(1, 10):
            print digits,[d],(len(A)-i)
            print digits + [d] * (len(A)-i)
            if digits + [d] * (len(A)-i) > A:
                print 'inside'
                digits.append(d-1)
                break
        else:
            digits.append(9)

    return int("".join(map(str, digits)))


print monotoneIncreasingDigits(332)
