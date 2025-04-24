from typing import List
from heapq import heapify,heappop

def removeKdigits(num: str, k: int) -> str:
    # if k >= len(num):
    #     return "0"
    # numlist = [int(x) for x in list(num)]
    # hnum = numlist.copy()
    # heapify(hnum)
    # currmin = heappop(hnum)
    # res = ""
    # for i in range(0,len(num)):
    #     if k == 0:
    #         res += num[i:]
    #         return res.lstrip("0") if len(res.strip("0")) != 0 else "0"
    #     if numlist[i] > currmin:
    #         k -= 1
    #     else:
    #         res += str(numlist[i])

    # return res.lstrip("0") if len(res.strip("0")) != 0 else "0"

    stack = []
        
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    stack = stack[:-k] if k > 0 else stack
    
    result = ''.join(stack).lstrip('0')
    
    return result if result else '0'           

if __name__ == '__main__':
    print(removeKdigits(num = "1432219", k = 3))
    print(removeKdigits(num = "10200", k = 1))
    print(removeKdigits(num = "10", k = 2))
    print(removeKdigits(num = "9", k = 1))
    print(removeKdigits(num ="112",k = 1))