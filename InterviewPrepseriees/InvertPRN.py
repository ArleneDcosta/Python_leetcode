from typing import List

def evalRPN(tokens: List[str]) -> int:
    nostack = []
    for ele in tokens:
        if ele in ["+","-","*","/"]:
            secondele = int(nostack.pop())
            firstele = int(nostack.pop())
            if ele == '+':
                result =  firstele + secondele
            elif ele == '-':
                result =  firstele - secondele
            elif ele == '*':
                result = firstele * secondele
            else:
                result = firstele / secondele
            nostack.append(result)
        else:
            nostack.append(ele)
    return nostack.pop()



if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    print(evalRPN(tokens))

    tokens = ["4","13","5","/","+"]
    print(evalRPN(tokens))

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))