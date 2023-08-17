# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    # Create a set of tuples to represent all possible domino tiles
    all_tiles = set()
    for i in range(0, 7):
        for j in range(i, 7):
            all_tiles.add((i, j))
    present_tiles = set()
    # Create a set of tuples to represent the tiles present in the grid
    for tile in A:
        e = tile.split('-')
        e = (int(e[0]), int(e[1]))
        present_tiles.add(e)
        e = (int(e[1]), int(e[0]))
        present_tiles.add(e)

    # Find the missing tile by subtracting the present tiles from all tiles
    missing_tile = list(all_tiles - present_tiles)
    missing_tile.sort(key=lambda x: x[0])

    val = missing_tile[0]
    res = f"{val[0]}-{val[1]}"
    return res