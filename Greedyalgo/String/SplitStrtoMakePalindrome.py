from typing import List

def checkPalindromeFormation(a: str, b: str, ) -> bool:
    n = len(a)
    i = 0
    while(i < n/2) and a[i] == b[n - i - 1]:
        i += 1
    j = 0
    while(j < n / 2) and b[j] == a[n - j - 1]:
        j += 1

    anchor = max(i,j)
    left = anchor
    right = n - 1 - anchor
    print(anchor)
    # Check ends above now the remaining central part u will check here
    while( right - left >= 1 and a[left] == a[right]):
        print(a[left],a[right],"INSIDE A")
        left += 1
        right -= 1

    if right - left < 1:
        return True

    left = anchor
    right = n - 1 - anchor
    while (right - left >= 1 and b[left] == b[right]):
        print(b[left], b[right], "INSIDE B")
        left += 1
        right -= 1

    if right - left < 1:
        return True

    return False
if __name__ == '__main__':
    # print(checkPalindromeFormation(a = "ulacfd", b = "jizalu"))
    print(checkPalindromeFormation(a="abda", b="acmc"))