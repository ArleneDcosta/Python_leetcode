from typing import List

#min(max(left),max(right)) - height

def trapold(height):
    maxheightleft = []
    maxele = 0
    for no in height:
        if no >= maxele:
            maxheightleft.append(no)
            maxele = no
        else:
            maxheightleft.append(maxele)

    maxheightright = []
    maxele = 0
    revheight = reversed(height.copy())
    for no in revheight:
        if no >= maxele:
            maxheightright.append(no)
            maxele = no
        else:
            maxheightright.append(maxele)

    maxheightright.reverse()

    print(maxheightleft,maxheightright)
    res = 0
    for i in range(len(height)):
        res += min(maxheightleft[i],maxheightright[i]) - height[i]
    return res

def trap(height):
    N = len(height)
    left = 0
    right = N - 1

    left_max = 0
    right_max = 0
    waters = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] <= left_max:
                waters += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if height[right] <= right_max:
                waters += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return waters

if __name__ == '__main__':
    print(trapold([0,1,0,2,1,0,1,3,2,1,2,1]))

    #https://leetcode.com/problems/trapping-rain-water/solutions/5945524/efficient-two-pointer-solution-beats-99-84/ check this for better soln