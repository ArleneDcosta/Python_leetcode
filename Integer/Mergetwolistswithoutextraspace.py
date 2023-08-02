def solve(arr1,arr2):
    arr1.sort()
    arr2.sort()
    i = 0
    j = 0
    while(i<len(arr1)):
        if arr1[i]>arr2[0]:
            #print i,j
            arr1[i],arr2[0]=arr2[0],arr1[i]
            arr2.sort()
        else:
            i+=1
            
    return arr1,arr2
        
    
print solve([0,2,6,8,9],[1,3,5,7])
print solve([5,8,9],[4,10,8])
