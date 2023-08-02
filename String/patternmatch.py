import re
def solve(s,p):
    res = re.match(r""+p+"",s)
    if res and res.group()== s:
        return True
    else:
        return False


print solve("aa","a*")
