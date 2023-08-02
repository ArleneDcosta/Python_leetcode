def solution(a, b):
    len = 0
    legs = 0
    pos = (a + b) // 4
    for i in range(pos, 0, -1):
        legs = (a // i) + (b // i)
        
        if (legs == 4):
            len = i
            break
        
    return len
    
print(solution(13, 10))
