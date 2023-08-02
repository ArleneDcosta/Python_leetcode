# Remember for Interval always sort by start or end
# If not sorting can do a line sweep
# In line sweep we have an infinte line and we add when we arrive and depart we minus
from collections import defaultdict

def split_painting(segments):
    points = defaultdict(int)

    for s,e,c in segments:
        points[s] += c
        points[e] -= c

    curTotal = s = 0
    ans  = []
    print(points)
    for i in range(10**5 + 5):
        if i in points:
            if curTotal:
                ans.append([s,i,curTotal])
            curTotal += points[i]
            s = i

    return ans

#####In case of common consideration if curr would be 0 it would mean that part is not overlapping and that would be considered
### else the entire would be considered as one interval
### but here it is opposite
##you could have checked where val is increasing ans = max(ans,currTotal) , and when currtotal = 0 update s and i will be e

if __name__ == '__main__':
    print(split_painting([[1,4,5],[1,6,6],[4,7,1],[4,7,7]]))
    print(split_painting([[1,4,5],[1,7,7]]))
    print(split_painting([[1,4,8],[6,10,2]]))

