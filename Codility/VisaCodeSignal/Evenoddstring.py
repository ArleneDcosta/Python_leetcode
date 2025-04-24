
def stringcheck(s):
    res = ""
    for i in range(0,len(s)):
        if i % 2 == 0:
            res += s[i].lower()
        else:
            if s[i].isalpha():
                currentchar = s[i]
                if currentchar == 'z':
                    nextchar = 'a'
                elif currentchar == 'Z':
                    nextchar = 'A'
                else:
                    nextchar = chr(ord(s[i]) + 1)
                res += nextchar
    return res

if __name__ == '__main__':
    print(stringcheck("Arkdfrrz"))