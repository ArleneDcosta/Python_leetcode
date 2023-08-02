def average(arr):
    return sum(arr)/len(arr)
def solve(arr,windowsize):
    result=[]
    avg=[]
    for ele in arr:
        if len(avg)<windowsize:
            avg.append(ele)
            result.append(average(avg))
        else:
            avg.pop(0)
            avg.append(ele)
            result.append(average(avg))
    return result

print solve([1,10,3,5],3)
