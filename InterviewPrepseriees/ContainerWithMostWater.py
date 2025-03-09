from typing import List


def maxArea(height: List[int]) -> int:
    left_pointer, right_pointer = 0, len(height) - 1
    while left_pointer < right_pointer:
        maxWater = max(maxWater, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
        if height[left_pointer] <= height[right_pointer]:
            left_pointer += 1
        else:
            right_pointer -= 1

    return maxWater

def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += max(0, right_max - height[right])

    return water_trapped


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))

