from typing import List
from collections import Counter

def smallestDistancePair(numbers: List[int], k: int) -> int:
    numbers.sort()
    minDistance, maxDistance = 0, numbers[-1] - numbers[0]
    
    while minDistance < maxDistance:
        midDistance = minDistance + (minDistance + maxDistance) // 2
        print(midDistance,countPairsWithinDistance(numbers, midDistance))
        if countPairsWithinDistance(numbers, midDistance) < k:
            minDistance = midDistance + 1
        else:
            maxDistance = midDistance
    
    return minDistance

def countPairsWithinDistance(numbers: List[int], targetDistance: int) -> int:
    count = left = 0
    for right in range(1, len(numbers)):
        while numbers[right] - numbers[left] > targetDistance:
            left += 1
        count += right - left
    return count


if __name__ == '__main__':
    print(smallestDistancePair(numbers = [1,3,1], k = 1))
    # print(smallestDistancePair(nums = [1,1,1], k = 2))
    # print(smallestDistancePair(nums=[1,6,1],k=3))
    # print(smallestDistancePair(nums = [62,100,4] , k = 2))