from typing import List
from collections import defaultdict

    
def advantageCount(nums1: List[int], nums2: List[int]) -> List[int]:
    # n1 = nums1.copy()
    # n2 = nums2.copy()
    # resultnum = []
    # n1.sort()
    # n2.sort()
    # resultdic = defaultdict(int)
    # for ele in n2:
    #     resultdic[ele],n1 = getclosestele(n1,ele)

    # if len(resultdic.keys()) < len(nums1):
    #     for i in range(0,len(nums2)):
    #         if resultdic[nums2[i]] != -1000:
    #             nums1[i] = resultdic[nums2[i]]
    #             resultdic[nums2[i]] = -1000
    #     return nums1

    # else:
    #     for ele in nums2:
    #         resultnum.append(resultdic[ele])

    # return resultnum
    sorted_nums1 = sorted(nums1)
    sorted_nums2 = sorted((num, i) for i, num in enumerate(nums2))
    print(sorted_nums1)
    print(sorted_nums2)
    res = [0] * len(nums1)
    remaining = []
    j = 0

    for num in sorted_nums1:
        if num > sorted_nums2[j][0]:
            res[sorted_nums2[j][1]] = num
            j += 1
        else:
            remaining.append(num)
            
    print(res,remaining)
    for i in range(len(nums2)):
        if res[i] == 0:
            res[i] = remaining.pop()

    return res



if __name__ == '__main__':
    # nums1 = [12,24,8,32]
    # nums2 = [13,25,32,11]
    # print(advantageCount(nums1,nums2))

    # nums1 = [2,7,11,15]
    # nums2 = [1,10,4,11]
    # print(advantageCount(nums1,nums2))

    # nums1 = [2,0,4,1,2]
    # nums2 =[1,3,0,0,2]
    # print(advantageCount(nums1,nums2))

    # nums1 = [2,0,4,1,2]
    # nums2 = [1,3,0,0,2]
    # print(advantageCount(nums1,nums2))

    nums1 = [8,2,4,4,5,6,6,0,4,7]
    nums2 = [0,8,7,4,4,2,8,5,2,0]
    print(advantageCount(nums1,nums2))