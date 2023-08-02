from collections import Counter
def subsetsWithDup(nums):
    powerset =[[]]
    hmap = Counter(nums);
    print(hmap)
    for key in hmap.keys():
        l = len(powerset)
        for i in range(0,len(powerset)):
            k = 0
            
            while( k < hmap[key] ):
                print(k,hmap[key])
                k+=1
                print(powerset,k*[key],k,powerset[i]+k*[key],i,len(powerset))
                powerset.append(powerset[i]+k*[key]);
    return powerset ;


print(subsetsWithDup([1,2,2]))

