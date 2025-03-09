from typing import List

def candy(ratings: List[int]) -> int:
    dpleft = [1] * len(ratings)
    dpright = [1] * len(ratings)
    result = 0

    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            dpright[i] = dpright[i-1] + 1

    for i in range(len(ratings)-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            dpleft[i] = dpleft[i+1] + 1

    for i in range(len(ratings)):
        result += max(dpleft[i],dpright[i])
    
    return result

if __name__ == '__main__':
    print(candy(ratings = [1,0,2]))
    print(candy(ratings = [1,2,2]))
    print(candy(ratings = [1,3,2,2,1]))




