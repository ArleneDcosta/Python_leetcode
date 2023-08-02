def solve(A):
    data = []    
    for s,e in A:
        data.append((s,1))
        data.append((e,-1))

    data.sort()
    print(data)
    curr = 0
    ans = 0
    for _,v in data:
        curr += v
        ans = max(ans,curr)
    return ans

if __name__ == '__main__':
    print(solve([[5,10],[15,20],[0,30]]))