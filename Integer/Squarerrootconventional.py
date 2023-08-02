def mySqrt(x):
    left = 0
    right = x

    if x==0 or x==1:
        return x

    while left <= right:
        mid = left + (right-left)//2
        testvalue = mid*mid

        if testvalue == x:
            return mid
        if testvalue < x:
            left = mid + 1
        else:
            right = mid -1

    return left-1
