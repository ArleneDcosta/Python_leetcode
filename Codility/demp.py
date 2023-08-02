def solution(N):
    for i in range(0,1000000):
        temp=list(map(int,list(str(i))))
        if sum(temp)==N:
            return i
    return 0
print solution(16)
print solution(19)
print solution(7)
