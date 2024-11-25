from typing import List


def isValid(s: str) -> bool:
    stk = []
    for char in s:
        if char == "(" or char == "[" or char == "{":
            stk.append(char)
        else:
            if len(stk) > 0:
                no = stk.pop()
                if char == ')' and no != "(":
                    return False
                if char == ']' and no != "[":
                    return False
                if char == '}' and no != "{":
                    return False
            else:
                return False
    if len(stk) != 0:
        return False
    return True

if __name__ == '__main__':
    print(isValid(s = "([])"))
    print(isValid(s = "(]"))
    print(isValid(s = "("))