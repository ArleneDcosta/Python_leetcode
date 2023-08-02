import collections as c
def minSetSize(arr):
    new=c.Counter(arr)
    n=len(arr)
    count=0
    ans=0
    new=sorted(new.values())[::-1]
    print new
    for i in new:
        count+=i
        ans+=1
        print count,ans,n//2
        if count>=n//2:
            return ans
print(minSetSize([3,3,3,3,5,5,5,2,2,7]))
