from typing import List


def maxEnvelopes(envelopes: List[List[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    print(envelopes)
    LIS = []
    size = 0
    for (w, h) in envelopes:
        if not LIS or h > LIS[-1]:
            LIS.append(h)
            size += 1
        else:
            l, r = 0, size
            while l < r:
                m = l + (r - l) // 2
                if LIS[m] < h: # h is too big for this spot
                    l = m + 1
                else:
                    r = m
            LIS[l] = h
    print(LIS)
    return size

if __name__ == '__main__':
    envelopes = [[6,4],[6,7],[7,4],[8,3]]
    print(maxEnvelopes(envelopes))