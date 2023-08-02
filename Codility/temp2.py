A=[1,3,6,4,1,2]

def solve(A):
    for i in range(1,100000):
        if i not in A:
            return i

print solve(A)
