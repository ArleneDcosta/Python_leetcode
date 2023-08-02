import re
def myAtoi(s):
    pattern = r"^\s*(-|\+)?\d+"
    match = re.match(pattern,s)
    if match:
        val = int(match.group())
        print(match.group(1))
    else:
        val = 0
    if val <= -2**31:
        return -2147483648
    elif val >= 2**31-1:
            return 2147483647
    elif val and val > -2**31 and val < 2**31 - 1:
        return val
    else:
        return 0
print myAtoi("-2147483647")
