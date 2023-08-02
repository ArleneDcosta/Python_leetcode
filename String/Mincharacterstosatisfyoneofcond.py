def minCharacters(self, a: str, b: str) -> int:
    c1, c2 =  [0]*26, [0]*26
    for ch in a:
        c1[ord(ch)-97] += 1
        
    for ch in b:
        c2[ord(ch)-97] += 1
        
    return min(
            #change all letters before curr letter to max and for c1
            #change greater to bring to the same value
            min(sum(c2[:i])+sum(c1[i:]) for i in range(1, 26)),
            min(sum(c1[:i])+sum(c2[i:]) for i in range(1,26)),
            sum(c1)-max(c1)+sum(c2)-max(c2)
        )
'''Your goal is to satisfy one of the following three conditions:

Every letter in a is strictly less than every letter in b in the alphabet.
Every letter in b is strictly less than every letter in a in the alphabet.
Both a and b consist of only one distinct letter.
Return the minimum number of operations needed to achieve your goal.'''
