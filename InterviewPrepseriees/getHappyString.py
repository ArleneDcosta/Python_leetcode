import collections

def getHappyString(n: int, k: int) -> str:
    # l = ['a','b','c']
    # res = ""
    # if k > ((2 ** (n-1)) * 3):
    #     return ""
    
    # if n == 1:
    #         if k <= len(l):
    #             return l[k-1]
    #         return res

    # while(n > 0):
    #     baseval = 2 ** (n-1)
    #     currentletter = l[k // baseval]
    #     if len(res) > 0 and currentletter == res[-1]:
    #         currentletter = l[((k // baseval)+1)% len(l)]
    #     res += currentletter
    #     k = k % baseval
    #     n = n - 1
    # return res
    nextLetter = {'a': 'bc', 'b': 'ac', 'c': 'ab'} 
    q = collections.deque(['a', 'b', 'c'])
    while len(q[0]) != n:
        u = q.popleft()
        print(u,u[-1],q)  
        for v in nextLetter[u[-1]]:
            q.append(u + v)
    return q[k - 1] if len(q) >= k else '' 


if __name__ == '__main__':
    # print(getHappyString(n=1,k=3))
    print(getHappyString(n=3,k=10))
    # print(getHappyString(n=2,k=1))
    # print(getHappyString(n=4,k=1))
    # print(getHappyString(n=2,k=7))