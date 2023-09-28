from typing import List

def findPermutation(s:str) -> List[int]:
    ans = []
    stack = []

    for i,c in enumerate(s):
        stack.append(i+1)

        if c == 'I':
            while stack:
                ans.append(stack.pop())
    stack.append(len(s) + 1)

    while stack:
        ans.append(stack.pop())

    return ans

if __name__ == '__main__':
    print(findPermutation("IID"))