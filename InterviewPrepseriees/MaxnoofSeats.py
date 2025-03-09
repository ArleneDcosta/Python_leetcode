from typing import List
from collections import defaultdict

def maxNumberOfFamiliesbf(n: int, reservedSeats: List[List[int]]) -> int:
    seats = [[1] * 10 for _ in range(0,n)]
    ans = 0
    for reserved in reservedSeats:
        seats[reserved[0]-1][reserved[1]-1] = 0

    for currentrow in seats:
        i = 1
        while(i < 6):
            if i == 2 or i == 4:
                i += 1
            if sum(currentrow[i:i+4]) == 4:
                ans += 1
                i = i + 4
            else:
                i += 1

    return ans

def maxNumberOfFamilies(n: int, reservedSeats: List[List[int]]) -> int:
    d = defaultdict(set)
    
    for row, seat in reservedSeats:
        d[row].add(seat)

    ans = 0

    for row in d:
        reserved = d[row]
        can_place = 0
        
        if not (2 in reserved or 3 in reserved or 4 in reserved or 5 in reserved):
            can_place += 1
        if not (6 in reserved or 7 in reserved or 8 in reserved or 9 in reserved):
            can_place += 1
        if can_place == 0 and not (4 in reserved or 5 in reserved or 6 in reserved or 7 in reserved):
            can_place = 1

        ans += can_place

    ans += (n - len(d)) * 2

    return ans

if __name__ == '__main__':
    print(maxNumberOfFamilies(n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]))
    print(maxNumberOfFamilies(n = 2, reservedSeats = [[2,1],[1,8],[2,6]]))
    print(maxNumberOfFamilies(n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]))
    print(maxNumberOfFamilies(n = 5,reservedSeats = [[4,7],[4,1],[3,1],[5,9],[4,4],[3,7],[1,3],[5,5],[1,6],[1,8],[3,9],[2,9],[1,4],[1,9],[1,10]]))
    print(maxNumberOfFamilies(n = 4,reservedSeats = [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]))