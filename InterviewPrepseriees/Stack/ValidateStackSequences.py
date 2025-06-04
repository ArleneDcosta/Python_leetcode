
from typing import List

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    resArr = []
    while len(popped) != 0:
        if resArr and resArr[-1] == popped[0]:
            resArr.pop()
            popped.pop(0)

        elif resArr and resArr[-1] != popped[0] and pushed and pushed[0] not in resArr:
            resArr.append(pushed.pop(0))
        elif len(resArr) == 0 and pushed[0] not in resArr:
            resArr.append(pushed.pop(0))
        else:
            return False

    return True


def validateStackSequencesOp(pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return not stack

if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    print(validateStackSequences(pushed,popped))

    pushed = [1,2,3,4,5]
    popped = [4,3,5,1,2]
    print(validateStackSequences(pushed,popped))

    pushed = [1,0]
    popped = [1,0]
    print(validateStackSequences(pushed,popped))