from collections import deque
def solve(height):
    left, right = deque(), deque()
    left_max, right_max = -100000, -10000
    water = 0
    for i in range(len(height)):
        left_max = max(left_max, height[i])
        left.append(left_max)
        right_max = max(right_max, height[len(height)-1-i])
        right.appendleft(right_max)
    print left,right
    for i in range(len(height)):
        water += (min(left[i], right[i]) - height[i])
    return water


print solve([0,1,0,2,1,0,1,3,2,1,2,1])
