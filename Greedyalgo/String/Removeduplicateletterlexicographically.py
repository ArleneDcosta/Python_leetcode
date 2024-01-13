from typing import List
from collections import Counter

'''
Add on stack
For coming check if current is lexically smaller than on stack 
If it is then remove the element from stack if counter is greater than 1 
else will remain in stack
'''
def removeDuplicateLetters(s: str) -> str:
    count = Counter(s)
    stack = []
    seen  = set()

    for c in s:
        count[c] -= 1
        if c in seen:
            continue
        while stack and c < stack[-1] and count[stack[-1]] > 0:
            removed = stack.pop()
            seen.remove(removed)

        stack.append(c)
        seen.add(c)

    return "".join(stack)

if __name__ == '__main__':
    print(removeDuplicateLetters("cbacdcbc"))
    print(removeDuplicateLetters("bdc"))