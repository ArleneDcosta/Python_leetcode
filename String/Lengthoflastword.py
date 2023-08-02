import re
def lengthOfLastWord(s):
    l = re.finditer(r"(?m)\w+",s)
    r = list(l)
    return len(r[-1].group())
   
print(lengthOfLastWord("   fly me   to   the moon  "))
print(lengthOfLastWord("luffy is still joyboy"))

