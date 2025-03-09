

def licenseKeyFormatting(s: str, k: int) -> str:
    splitString = s.split("-")
    resultString = ""
    fullString  = "".join(splitString)
    first_group_len = len(fullString) % k

    resultString += fullString[0:first_group_len]
    resultString += "-"

    currcount = 1
    for i in range(first_group_len,len(fullString)):
        resultString += fullString[i]
        if  currcount % k == 0:
            resultString += "-"
            currcount = 1
        else:
            currcount += 1

    return resultString.upper().strip("-")

def licenseKeyFormatting(S,K):
    S = S.replace("-", "").upper()[::-1]
    return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]

if __name__ == '__main__':
    print(licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4))
    print(licenseKeyFormatting(s = "2-5g-3-J", k = 2))
    print(licenseKeyFormatting(s ="2-4A0r7-4k",k =4))