def check(arr1,arr2):
    i=0
    j=0
    out=[]
    diff=29999
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            if abs(arr2[j]-arr1[i])<diff:
                diff = abs(arr2[j]-arr1[i])
                out=[arr1[i],arr2[j]]
            i+=1
            
        else:
            if abs(arr2[j]-arr1[i])<diff:
                diff = abs(arr2[j]-arr1[i])
                out=[arr1[i],arr2[j]]
            j+=1
        
    return out
print check([-1,3,5,10,20,28],[15,17,26,134,135])
