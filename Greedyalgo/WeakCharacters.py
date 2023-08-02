from typing import List
def numberOfWeakCharacters(properties: List[List[int]]) -> int:
    properties.sort(key = lambda x:(-x[0],x[1]))
    print(properties)
    ans = mmax = 0

    for a,d in properties:
        if d < mmax:
            ans += 1

        mmax = max(mmax,d)

    return ans

if __name__ == '__main__':
    print(numberOfWeakCharacters([[0,6],[1,7],[1,6],[2,5],[2,6]]))
    print(numberOfWeakCharacters([[5,5],[6,3],[3,6]]))
