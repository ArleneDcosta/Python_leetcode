from typing import List
import math

def checkobstacle(currentcood,obstacles,direction,command):
    for _ in range(command):
        if direction == 'n':
            next_pos = (currentcood[0], currentcood[1] + 1)
        elif direction == 'e':
            next_pos = (currentcood[0] + 1, currentcood[1])
        elif direction == 's':
            next_pos = (currentcood[0], currentcood[1] - 1)
        elif direction == 'w':
            next_pos = (currentcood[0] - 1, currentcood[1])

        if next_pos in obstacles:
            return currentcood  

        currentcood = list(next_pos)

def robotSim(commands: List[int], obstacles: List[List[int]]) -> int:
    d = ['n','e','s','w']
    i = 0
    cood = [0,0]
    furthestpoint = 0

    obstacles = set(map(tuple, obstacles))
    for command in commands:
        if command == -1:
            i = (i+1)% len(d)
        elif command == -2:
            i = (i-1) % len(d)

        else:
            cood = checkobstacle(cood, obstacles ,d[i],command)
            currval = cood[0] ** 2 + cood[1] ** 2 
            furthestpoint = max(currval,furthestpoint)

    return furthestpoint


if __name__ == '__main__':
    print(robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
    print(robotSim(commands = [4,-1,3], obstacles = []))
    print(robotSim(commands = [6,-1,-1,6], obstacles = [[0,0]]))