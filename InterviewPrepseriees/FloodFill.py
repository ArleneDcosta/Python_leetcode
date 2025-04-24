from typing import List
from collections import deque

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    r = len(image)
    c = len(image[0])
    visited = set()
    visited.add((sr,sc))
    queue = deque()
    queue.append((sr,sc))
    while queue:
        current_block = queue.popleft()
        print(current_block)
        image[current_block[0]][current_block[1]] = color
        if current_block[0] - 1 >= 0 and (current_block[0] - 1,current_block[1]) not in visited and image[current_block[0] - 1][current_block[1]] != 0:
            visited.add((current_block[0] - 1,current_block[1]))
            queue.append((current_block[0] - 1,current_block[1]))

        if current_block[1] - 1 >= 0 and (current_block[0],current_block[1] - 1) not in visited and image[current_block[0]][current_block[1] - 1] != 0:
            visited.add((current_block[0],current_block[1] - 1))
            queue.append((current_block[0],current_block[1] - 1))

        if current_block[0] + 1 <= r - 1 and (current_block[0] + 1,current_block[1]) not in visited and image[current_block[0] + 1][current_block[1]] != 0:
            visited.add((current_block[0] + 1,current_block[1]))
            queue.append((current_block[0] + 1,current_block[1]))

        if current_block[1] + 1 <= c - 1 and (current_block[0],current_block[1] + 1) not in visited and image[current_block[0]][current_block[1] + 1] != 0:
            visited.add((current_block[0],current_block[1] + 1))
            queue.append((current_block[0],current_block[1] + 1))

    return image

if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))
