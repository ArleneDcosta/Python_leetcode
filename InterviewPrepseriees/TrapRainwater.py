from typing import List

#min(max(left),max(right)) - height

def trap(height):
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

    res = 0
    for i in range(len(height)):
        res += min(maxheightleft[i],maxheightright[i]) - height[i]
    return res

if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))

    #https://leetcode.com/problems/trapping-rain-water/solutions/5945524/efficient-two-pointer-solution-beats-99-84/ check this for better soln