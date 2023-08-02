def solve(n):
    l = bin(n)[2:]
    distance = 0
    sum = 0
    for i in range(0,len(l)):
        if l[i] == '1':
            sum+=1
        elif l[i]== '0':
            sum = 0
            
        distance = max(distance,sum)
        
    return distance



print solve(22)
