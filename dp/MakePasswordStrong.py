from typing import List
from functools import lru_cache
import sys

def strongPasswordChecker(password: str) -> int:
    @lru_cache(None)
    def dp(index,numOfChr,hasLower,hasUpper,hasDigit,lastChr,secondLastChr):
        if numOfChr > 20:
            return sys.maxsize
        if index == n:
            if numOfChr >= 6 and hasLower and hasDigit and hasUpper:
                return 0
            else:
                return sys.maxsize

        ans = sys.maxsize
        #keep( if satisfies all the conditions)
        if password[index]!= lastChr or password[index] != secondLastChr:
            ans = min(ans,dp(index+1,numOfChr + 1,
                             hasLower or password[index].islower(),
                             hasUpper or password[index].isupper(),
                             hasDigit or password[index].isdigit(),
                             password[index],lastChr
                             ))
        #insert lowercase
        ans = min(ans, dp(index, numOfChr + 1,
                          True,
                          hasUpper,
                          hasDigit,
                          'y' if lastChr == 'z' else 'z', lastChr) +1)

        #insert upper case
        ans = min(ans, dp(index, numOfChr + 1,
                          hasLower,
                          True,
                          hasDigit,
                          'Y' if lastChr == 'Z' else 'Z', lastChr) + 1)
        #insert digit

        ans = min(ans, dp(index, numOfChr + 1,
                          hasLower,
                          hasUpper,
                          True,
                          '8' if lastChr == '9' else '9', lastChr) + 1)

        # change to lowercase
        ans = min(ans, dp(index + 1, numOfChr + 1,
                          True,
                          hasUpper,
                          hasDigit,
                          'y' if lastChr == 'z' else 'z', lastChr) + 1)

        # change to upper case
        ans = min(ans, dp(index + 1, numOfChr + 1,
                          hasLower,
                          True,
                          hasDigit,
                          'Y' if lastChr == 'Z' else 'Z', lastChr) + 1)
        # change to digit

        ans = min(ans, dp(index + 1, numOfChr + 1,
                          hasLower,
                          hasUpper,
                          True,
                          '8' if lastChr == '9' else '9', lastChr) + 1)
        #delete
        ans = min(ans, dp(index + 1, numOfChr,
                          hasLower,
                          hasUpper,
                          hasDigit,
                          lastChr, secondLastChr) + 1)
        return ans
    n = len(password)
    if n == 0:
        return 6
    return dp(0,0,False,False,False,'','')


if __name__ == '__main__':
    print(strongPasswordChecker("1337cadfddfdfdfd0d3"))
    password = "1337c0d3"
    #password = "aA1"
    #a