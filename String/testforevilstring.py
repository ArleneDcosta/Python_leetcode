def failure(pat): 
    res = [0]
    i, target = 1, 0
    while i < len(pat): 
        if pat[i] == pat[target]: 
            target += 1
            res += target,
            i += 1
        elif target: 
            target = res[target-1] 
        else: 
            res += 0,
            i += 1
    return res    

print(failure('leet'))
