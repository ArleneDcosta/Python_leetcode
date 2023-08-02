def closestDivisors(num):
    for i in range(int(round((num+1))**(0.5))+1, 0,-1):
        if (num+1)%i == 0:
            ans = [(num+1)//i, i]
            break
    for j in range(int(round((num+2))**(0.5))+1, 0,-1): 
        if (num+2)%j == 0:
            if abs((num+2)//j - j) < abs(ans[0]-ans[1]):
                ans = [(num+2)//j, j]
            break
    return ans


print closestDivisors(8)
print closestDivisors(123)
print closestDivisors(999)
