from typing import List

def maxDistance(position: List[int], m: int) -> int:
    #Here m is the no of baskets to place the ball
    def count(d):
        #Here d is lowerbound
        #As soon criteria is passed the current i is considered
        ans,pre_pos = 1, position[0]
        for i in range(1,n):
            if position[i] - pre_pos >= d:
                ans += 1
                pre_pos = position[i]
        return ans

    n = len(position)
    position.sort()
    left = 1
    right = position[-1] - position[0]
    while(left < right):
        mid = left + (right - left + 1)//2
        print(mid,count(mid))
        if count(mid) >= m: #includes mid
            left  = mid
        else:
            right = mid - 1

    return left


#maximum minimum force(similiar to sweetness finder)
if __name__ == '__main__':
    print(maxDistance([1,2,3,4,7],3))