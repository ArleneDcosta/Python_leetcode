from typing import List

#logic: Convert 2D into 1D and later swap
#Use Trailing 0 logic

def minSwaps(grid: List[List[int]]) -> int:
    ans = 0
    n = len(grid)
    tr = []

    # Get trailing 0's for each row
    for row in grid:
        count = 0
        for i in range(n-1,-1,-1):
            if row[i] == 0:
                count += 1
            else:
                break
        tr.append(count)

    for i,count in enumerate(tr):
        target = n - i - 1
        print(target,'ddfd')
        k = i
        while k < n and tr[k] < target:
            k += 1
        if k == n:
            return -1

        ans += k - i

        while k > i:
            tr[k],tr[k-1] = tr[k-1],tr[k]
            print("Inside while",tr)
            k -= 1

    return ans

if __name__ == '__main__':
    print(minSwaps([[0,0,1],[1,1,0],[1,0,0]]))