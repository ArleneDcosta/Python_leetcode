def letterCombinations(digits):
    letters = {'2': ['a', 'b', 'c'],'3': ['d', 'e', 'f'],'4': ['g', 'h', 'i'],'5': ['j', 'k', 'l'],'6': ['m', 'n', 'o'],'7': ['p', 'q', 'r', 's'],'8': ['t', 'u', 'v'],'9': ['w', 'x', 'y', 'z']}

    def backtrack(start):
        if digits == "":
            return []
        if len(tempList) == len(digits):
            res.append("".join(tempList))
            return
        chars = letters[digits[start]]
        for i in range(len(chars)):
            tempList.append(chars[i])
            backtrack(start + 1)
            tempList.pop()

    res = []
    tempList = []
    backtrack(0)
    return res
