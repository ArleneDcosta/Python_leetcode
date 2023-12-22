from typing import List
from functools import lru_cache
import sys
'''
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
'''
'''
Logic:
Case n > 20:
    Make string a multiple of 3 so that the best string can be obtained:
    aaaaaaa so delete last a and aaaaaa then replace both a's with a digit or something else
    Check if n%3 == 0 and n % 3 == 1
n < 6:
6 - n ( Minimum things needed to be added) if correct , miss_type eg: aaaaa then it would be 1 but ehre aabaa + 1
max(6-n,miss_types)

for n > 6 and n < 20:
max( miss_types , changes ) 

'''
def strongPasswordChecker(password: str) -> int:
    n = len(password)
    missing_types = 3
    if any(c.islower() for c in password):
        missing_types -= 1
    if any(c.isupper() for c in password):
        missing_types -= 1
    if any(c.isdigit() for c in password):
        missing_types -= 1

    change = 0
    remove_one  = 0
    remove_two = 0
    i = 2
    while(i < n):
        if password[i] == password[i-1] == password[i-2]:
            length = 2
            while i < n and password[i] == password[i-1]:
                length += 1
                i += 1
            print(length, length % 3)
            # to replace the character like aaaaaa at the 2 and 5 index
            change += length // 3
            # but when u remove one we get aaaaa so u have to only change 1 so remove 1
            if length % 3 == 0:
                remove_one += 1
            elif length % 3 == 1:
                remove_two += 1
        else:
            i += 1
    if n < 6:
        return max(missing_types, 6 - n)
    elif n <= 20:
        return max(missing_types,change)
    else:
        deletes = n - 20
        # aaaaaa so if we remove one so we have to change one or else 2
        # 8 - 1 = 7[ as that one change is getting covered in delete]
        change -= min(deletes, remove_one)
        # below case is only for remove 2 or else it will be 0 for every removing 2
        # aaaaaaa
        # 7 - 0
        change -= min(max(deletes - remove_one,0), remove_two * 2) // 2
        # 7 - ( 4 - 1)//3 = 6[ Remaining
        # So from total changes remain 7, we are removing  4 - 1(remove_one as aldready TBD for red change no)
        # As change is also getting covered in delete
        change -= max(deletes - remove_one - remove_two * 2,0) // 3
        return deletes + max(missing_types,change)

if __name__ == '__main__':
    #print(strongPasswordChecker("1337cadfddfdfdfd0d3"))
    print(strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaaaa"))
    password = "1337c0d3"
    #password = "aA1"
    #a