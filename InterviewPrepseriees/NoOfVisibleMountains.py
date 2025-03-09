import sys
from collections import Counter

def countMountains(peaks):
    foot = []
    for peak in peaks:
        foot.append((peak[0] - peak[1],peak[0] + peak[1]))
    foot.sort(key=lambda x: (x[0], -x[1]))
    print(foot)
    cnt = Counter(foot)
    ans,cur  = 0, -sys.maxsize
    for l,r in foot:
        if r <= cur:
            continue
        curr = r
        if cnt[(l,r)] not in cnt:
            ans += 1

    return ans

if __name__ == '__main__':
    print(countMountains(peaks = [[2,2],[6,4],[5,4]]))