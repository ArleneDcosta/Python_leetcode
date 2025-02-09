from typing import List
import collections

def checkIfCanBreak(s1: str, s2: str) -> bool:
    x = list(s1)
    y = list(s2)
    x.sort()
    y.sort()

    res = []
    for i in range(len(x)):
        res.append(ord(x[i]) - ord(y[i]))

    firstsign = -100

    for ele in res:
        if firstsign == -100 and ele != 0:
            if ele > 0:
                firstsign = 1
            else:
                firstsign = 0
        if ele != 0:
            if ele < 0 and firstsign == 1:
                return False
            elif ele > 0 and firstsign == 0:
                return False
    
    return True


def check(d1, d2):
    s = 0
    for c in 'abcdefghijklmnopqrstuvwxyz':
        s += d1[c] - d2[c]
        if s < 0:
            return False
    return True
    
def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    d1 = collections.Counter(s1)
    d2 = collections.Counter(s2)
    return self.check(d1, d2) | self.check(d2, d1)

if __name__ == '__main__':
    s1 = "abc"
    s2 = "xya"
    print(checkIfCanBreak(s1,s2))

    s1 = "abe"
    s2 = "acd"
    print(checkIfCanBreak(s1,s2))

    s1 = "leetcodee"
    s2 = "interview"
    print(checkIfCanBreak(s1,s2))