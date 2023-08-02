scrambles  = {}
def isScramble(s1, s2):
    #memoization
    if (s1, s2) in scrambles:
        return scrambles[(s1, s2)]
    if s1 == s2:
        scrambles[(s1, s2)] = True
        return True
    ls = len(s1)
    if ls == 1 or sorted(s1) != sorted(s2):
        scrambles[(s1, s2)] = False
        return False

    for i in range(1, ls):
        print('top',i,s1[:i], s1[i:],s2[:i], s2[i:])
        s1_left, s1_right = s1[:i], s1[i:]
        s2_left, s2_right = s2[:i], s2[i:]
        match1 = isScramble(s1_left, s2_left) and isScramble(s1_right, s2_right)
        print('bottom',i,ls,s2[:ls - i], s2[ls - i:])
        #Switch step
        s2_left2, s2_right2 = s2[:ls - i], s2[ls - i:]
        match2 = isScramble(s1_left, s2_right2) and isScramble(s1_right, s2_left2)
        print(i,match1,match2,s1,s2)
        if match1 or match2:
            scrambles[(s1, s2)] = True
            return True
            
    scrambles[(s1, s2)] = False
    return False

print(isScramble(s1 = "great", s2 = "rgeat"))
