def merge(intervals):
    result = []
    intervals = sorted(intervals, key=lambda x:x[0])
    result.append(intervals[0])
    intervals.pop(0)
    while len(intervals) > 0:
        lastval = result[-1]
        s1 = lastval[0]
        e1 = lastval[1]
        s2 = intervals[0][0]
        e2 = intervals[0][1]
        if s1 <= s2 and s2 <= e1 and e1 <= e2:
            result.pop(len(result)-1)
            if [s1,e2] not in result:
                result.append([s1,e2])
            intervals.pop(0)
        elif s1 <= s2 and s2 <= e1 and e2 <= e1:
            result.pop(len(result)-1)
            if [s1,e1] not in result:
                result.append([s1,e1])
            intervals.pop(0)
        else:
            if [s2,e2] not in result:
                result.append([s2,e2])
            intervals.pop(0)
    return result
        

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))
print(merge([[1,4],[1,4]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,4],[2,3]]))
