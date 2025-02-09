
def convert(s: str, numRows: int) -> str:
    # res = []

    # for i in range(0,numRows):
    #     res.append([])

    # j = 0
    # flag = 1

    # for i in range(0,len(s)):
    #     if j >= numRows:
    #         j = numRows - 1
    #     res[j].append(s[i])
    #     if numRows - 1 == j:
    #         flag = 0
        
    #     if j == 0:
    #         flag = 1 

    #     if flag == 1:
    #         j += 1
    #     else:
    #         j -= 1

    # finalres = ""

    # for ele in res:
    #     finalres += "".join(ele)

    template = list(range(numRows)) + list(range(numRows - 2, 0, -1))
    print(template)

    result = [''] * numRows
    for i, char in enumerate(s):
        result[template[i % len(template)]] += char
    return ''.join(result)
    # return finalres

if __name__ == '__main__':
    print(convert(s = "PAYPALISHIRING", numRows = 3))
    print(convert(s = "PAYPALISHIRING", numRows = 4))
    print(convert(s = "AB", numRows = 1))