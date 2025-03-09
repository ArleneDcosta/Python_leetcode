from typing import List

def shipWithinDays(weights: List[int], days: int) -> int:
    def helper(weight):
        totalcnt = 0
        i = 0
        currsum = 0
        while(i < len(weights)):
            currsum += weights[i]
            if currsum == weight:
                totalcnt += 1
                currsum = 0
            if currsum >= weight:
                totalcnt += 1
                currsum = weights[i]

            i += 1

        if currsum == 0:
            return totalcnt
        return totalcnt + 1

    # print(helper(7))
    left = max(weights)
    right = sum(weights)
    while(left < right):
        mid = left + (right - left) // 2
        print(mid,left,right)
        if helper(mid) <= days:
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    # print(shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
    # print(shipWithinDays(weights = [3,2,2,4,1,4], days = 3))
    # print(shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 10))
    print(shipWithinDays(weights = [3,3,3,3,3,3], days = 2))