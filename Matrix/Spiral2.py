def soln(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    upper, lower = 0, n-1
    left, right = 0, n-1
    num = 1
    while upper<=lower and left <= right:
        for i in range(left, right+1):   # 1st for loop
            res[upper][i] = num
            num += 1
        upper += 1
            
        for j in range(upper, lower+1):    # 2nd for loop
            res[j][right] = num 
            num += 1
        right -= 1
            
        if upper<=lower:
            for i in range(right, left-1, -1):     # 3rd for loop
                res[lower][i] = num
                num += 1
            lower -= 1
            
        if left <= right:
            for j in range(lower, upper-1, -1):     # 4th for loop
                res[j][left] = num
                num += 1
            left += 1
        
    return res
    
print(soln(3))
