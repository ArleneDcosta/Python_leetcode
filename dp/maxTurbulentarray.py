from typing import List
#Works for consecutive values

#More concise code
def maxTurbulenceSize(arr: List[int]) -> int:
    n = len(arr)
    greater = 1
    smaller = 1
    ans = 1

    for i in range(1,n):
        greater1 = smaller1  = 1
        if arr[i] > arr[i-1]:
            greater1 = smaller + 1
        elif arr[i] < arr[i-1]:
            smaller1 = greater + 1

        ans =  max(ans,greater1,smaller1)
        greater,smaller = greater1,smaller1
    return ans

def maxTurbulenceSizeold(arr: List[int]) -> int:
    n = len(arr)
    ans = res = 1
    for i in range(1,n):
        if i % 2 == 0 :
            if arr[i] <= arr[i-1]:
                ans = 1
            elif arr[i] > arr[i-1]:
                ans +=1
        elif i % 2 != 0 :
            if arr[i] >= arr[i-1]:
                ans = 1
            elif arr[i] < arr[i-1]:
                ans +=1
        res = max(ans,res)
    ans = 1
    for i in range(1,n):
        if i % 2 == 0 :
            if arr[i] >= arr[i-1] :
                ans = 1
            elif arr[i] < arr[i-1] :
                ans +=1

        elif i % 2 != 0 :
            if arr[i] <= arr[i-1] :
                ans = 1
            elif arr[i] > arr[i-1] :
                ans +=1
        res = max(ans,res)
    return res


if __name__ == '__main__':
    print(maxTurbulenceSizeold([9,4,2,10,7,8,8,1,9]))
    print(maxTurbulenceSizeold([4,8,12,16]))
