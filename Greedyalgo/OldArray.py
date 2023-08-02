from typing import List
from collections import Counter
import time

def findOriginalArray(changed: List[int]) -> List[int]:

    n = len(changed)
    if n % 2:
        return []
    count = Counter(changed)
    start = time.time()
    changed.sort()
    ans  = []
    for num in changed:
        if num == 0 and count[num] >= 2:
            count[num] -= 2
            ans.append(num)
        elif num > 0 and count[num] and count[num*2]:
            count[num] -= 1
            count[num*2] -= 1
            ans.append(num)
    end =  time.time()
    diff = end - start
    #print(diff)
    return ans if len(ans) == n // 2 else []

#main function and .remove takes a lot more time as O(n) is the time complexity
def findOriginalArraynaive(changed: List[int]) -> List[int]:
    originalLength = len(changed)
    newLength = 0
    result = []
    start = time.time()
    changed.sort()
    while len(changed) > 0:
        ele = changed[0]
        #print(ele,changed)
        if ele * 2 in changed :
            #print(changed,ele,ele*2)
            changed.remove(ele * 2)
            if ele in changed:
                changed.remove(ele)

                result.append(ele)
            else:
                return []

        newLength = len(changed)
        if originalLength == newLength:
            return []
        originalLength = newLength
    end = time.time()
    diff = end - start
    #print(diff)
    return result

if __name__ == '__main__':
    print(findOriginalArraynaive([4,2,0]))
    #print(findOriginalArraynaive([6,3,0,1]))
    #print(findOriginalArraynaive([1,3,4,2,6,8]))