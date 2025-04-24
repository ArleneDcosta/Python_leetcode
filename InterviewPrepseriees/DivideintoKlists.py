
from typing import List
from collections import Counter

def isPossibleDivide(nums: List[int], k: int) -> bool:
    # if len(nums) % k != 0:
    #     return False
    

    # numofsets = len(nums)//k
    # cnt = Counter(nums)
    # nums = sorted(nums)
        

    # resultlist = []
    # for i in range(0,len(nums)//k):
    #     resultlist.append([])
    
    # covered = 0
    # for num in cnt:
    #     i = covered
    #     while cnt[num]!=0:
    #         resultlist[i].append(num)
    #         cnt[num] -= 1
    #         if len(resultlist[i]) >= k:
    #             covered += 1
    #         i = (i+1) % numofsets
    # print(resultlist)

    # if covered != numofsets:
    #     return False
    
    # for result in resultlist:
    #     currentmax = max(result)
    #     for num in result:
    #         if num != currentmax and num + 1 not in result:
    #             return False
    

    # return True
    c = Counter(nums)
    print(c)
    for i in sorted(c):
        if c[i] > 0:
            for j in range(k)[::-1]:
                print(i,j,c[i+j],c[i])
                c[i + j] -= c[i]
                if c[i + j] < 0:
                    return False
    return True


if __name__ == '__main__':
    # print(isPossibleDivide(nums = [1,2,3,3,4,4,5,6], k = 4))
    # print(isPossibleDivide(nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3))
    # print(isPossibleDivide(nums = [16,21,26,35],k = 4))
    print(isPossibleDivide(nums = [10,9,8,1,2,3,2,3,4,4,5,6,10,11,12], k = 3))