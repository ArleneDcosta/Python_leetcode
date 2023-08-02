def solve(s):
    #left to right )
    left = right = maxlength = 0;
    for i in range(0,len(s)):
        if (i < len(s) and s[i] == '('):
            left+=1
        else:
            right+=1
            
        if (left == right):
            maxlength = max(maxlength, 2 * right);
        elif (right >= left):
            left = right = 0
    #print(maxlength)       

    #right to left  (   
    left = right = 0
    for i in range(len(s)-1,-1,-1):
        if (i < len(s) and s[i] == '('):
            left+=1
        else:
            right+=1
        print(left)
            
        if (left == right):
            maxlength = max(maxlength, 2 * left)
        elif (left >= right):
            left = right = 0
            
        
    return maxlength
print solve("(()")#here right to left makes sense
print solve(")()())")#here left to right makes sense
