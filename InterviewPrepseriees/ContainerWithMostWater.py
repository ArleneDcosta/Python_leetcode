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

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))

