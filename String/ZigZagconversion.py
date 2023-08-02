def convert(s, numRows):
 
    lin = 0
    pl = 1
    outp = [""] * numRows
    print(outp)
    for i in range(len(s)):
        outp[lin] += s[i]
        if numRows > 1:
            lin += pl
            if lin == 0 or lin == numRows -1:
                pl *= -1
    outputStr = ""
    for j in range(numRows):
        outputStr += outp[j]
    return outputStr 
print convert(s = "PAYPALISHIRING", numRows = 3)
