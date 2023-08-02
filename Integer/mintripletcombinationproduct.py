def solve(arr):
    arr.sort()
    index = len(arr)-1
    for i in range(0,len(arr)):
        if arr[i]>=0:
            index = i
            break
    if index == len(arr)-1 or index == 0:
        return arr[0]*arr[1]*arr[2]
    else:
        return arr[0]*arr[len(arr)-1]*arr[len(arr)-2]

print solve([4,-1,3,5,9])  
