from typing import List
from collections import Counter, defaultdict

def minCostToMoveChips(position: List[int]) -> int:
    even_parity = 0
    odd_parity = 0
    for chip in position:
        if chip % 2 == 0:
            even_parity += 1
        else:
            odd_parity += 1
    return min(even_parity, odd_parity)

if __name__ == '__main__':
    position = [2,2,2,3,3]
    print(minCostToMoveChips(position))

    position = [1,1000000000]
    print(minCostToMoveChips(position))

    position = [1,2,3]
    print(minCostToMoveChips(position))