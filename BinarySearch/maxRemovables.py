

def maximumRemovables(s,p,removable):
    def canRemove(mid):
        j = 0 #pointer of p
        removeSet =  set(removable[:mid+1])
        n1 = len(s)
        n2 = len(p)
        print(removeSet)
        for i in range(n1):
            if i not in removeSet and s[i] == p[j]:
                j+=1
                if j == n2:
                    return True

        return False

    n = len(removable)
    l = 0
    r = n - 1
    while (l < r):
        #Here problems may arise for 1 and 0
        mid = l + ( r - l + 1 ) // 2
        print(mid,l,r)
        if canRemove(mid):
            l = mid
        else:
            r = mid - 1

    return l + 1 if canRemove(l) else 0

print(maximumRemovables("abcbddddd","abcd",[3,2,1,4,5,6]))
#print(0 + 1//2)