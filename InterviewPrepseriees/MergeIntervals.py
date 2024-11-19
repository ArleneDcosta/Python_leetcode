from typing import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    sortedlist = sorted(intervals, key=lambda x: x[0])
    res = [sortedlist[0]]
    i = 1
    residx = 0
    while (i < len(intervals)):
        currinterval = res[residx]
        nextinterval = sortedlist[i]
        if currinterval[1] >= nextinterval[0] and nextinterval[1] >= currinterval[1]:
            res[residx] = [currinterval[0], nextinterval[1]]
            i += 1
        elif currinterval[0] == nextinterval[0] and currinterval[1] == nextinterval[1]:
            res[residx] = [currinterval[0], nextinterval[1]]
            i += 1
        elif currinterval[1] > nextinterval[0] and currinterval[0] <= nextinterval[1]:
            res[residx] = [currinterval[0], currinterval[1]]
            i += 1
        else:
            res.append(nextinterval)
            i += 1
            residx += 1

    return res