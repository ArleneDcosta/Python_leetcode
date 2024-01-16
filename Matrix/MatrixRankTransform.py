from typing import List
from collections import defaultdict

def matrixRankTransform(matrix: List[List[int]]) -> List[List[int]]:
    m = len(matrix)
    n = len(matrix[0])

    def find(x):
        if x!= parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x,y):
        r1 = find(x)
        r2 = find(y)
        if r1 != r2:
            parents[r1] = r2
    value2Pos = defaultdict(list)

    for i in range(m):
        for j in range(n):
            val = matrix[i][j]
            value2Pos[val].append((i,j))
    ans  = [[0] * n for _ in range(m)]
    rowMaxRank = [0] * m
    colMaxRank = [0] * n
    print(value2Pos)
    for val in sorted(value2Pos):
        print(val)
        parents = list(range(m+n))
        # Group numbers on the same row/col and get a unique value for later access (row + col) if present on the same row and col
        for i,j in value2Pos[val]:
            print(i,j+n,val)
            union(i,j+n)
        print(parents)
        root2Rank = defaultdict(int)

        #calculate new rank for the nums which have the same root ( on the same row/col )
        for i,j in value2Pos[val]:
            root = find(i)
            # Max is considered incase there is another the same value in another row-col due to combination
            root2Rank[root] = max(root2Rank[root],max(rowMaxRank[i],colMaxRank[j]) + 1)

        #update the ans and row/colMaxRank
        for i, j in value2Pos[val]:
            root = find(i)
            rank = root2Rank[root]
            ans[i][j] = rank
            rowMaxRank[i] = rank
            colMaxRank[j] = rank

        print(ans[i][j],i,j)
        print("Row max rank", rowMaxRank, colMaxRank, root2Rank)
    return ans


if __name__ == '__main__':
    print(matrixRankTransform([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))