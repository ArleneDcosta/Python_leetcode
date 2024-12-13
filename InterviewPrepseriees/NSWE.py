def solve(string):
    # Define movement directions as a dictionary
    direction_map = {
        'N': (0, 1),  # North increases y by 1
        'S': (0, -1),  # South decreases y by 1
        'E': (1, 0),  # East increases x by 1
        'W': (-1, 0)  # West decreases x by 1
    }

    # Initialize position at the origin (0, 0)
    x, y = 0, 0

    # To track direction cancellations
    move_history = []

    # Process each character in the string
    for char in string:
        if char in direction_map:
            dx, dy = direction_map[char]
            x += dx
            y += dy

            # Check if the current move cancels out the last move
            if move_history and move_history[-1] == (dx, dy):
                # Cancel out move (we ignore the invalid canceling movement)
                continue
            elif move_history and (move_history[-1] == (-dx, -dy)):
                # This cancels the current move, invalidate loop
                move_history.pop()  # Remove the last valid move
            else:
                # Store the current valid move
                move_history.append((dx, dy))

        else:
            return False  # Invalid direction found

    # If we are at the origin after all movements, return True (valid loop)
    return (x, y) == (0, 0) and len(move_history) == 0

def solve1(string):
    res = 0
    dir = {'N':1,'S':-1,'E':2,'W':-2}

    countdir = {}
    for chr in string:
        if chr in countdir:
            countdir[chr] += 1
        else:
            countdir[chr] = 1
    countchr = list(set(countdir.values()))

    for ele in string:
        if ele in dir:
            res += dir[ele]
        else:
            return False
    if res == 0:
        if len(countchr) == 1:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(solve1("NSEW"))
    print(solve1("NSEWWE"))
