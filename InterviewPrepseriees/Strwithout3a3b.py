
from typing import List

def strWithout3a3b(a: int, b: int) -> str:
    '''if a > b:
        flag = 'a'
        d = {'a': a, 'b': b}
    else:
        flag = 'b'
        d = {'b': b, 'a': a}
    res =""
    totalreslen = a + b
    while len(res) < totalreslen :
        for char in d.keys():
            if char == flag:
                value = min(d[char],2)
            else:
                value = min(d[char],1)
            res += char * value
            d[char] -= value

    return res'''
    ans = []
    A = a
    B = b

    while A or B:
        if len(ans) >= 2 and ans[-1] == ans[-2]:
            writeA = ans[-1] == 'b'
        else:
            writeA = A >= B

        if writeA:
            A -= 1
            ans.append('a')
        else:
            B -= 1
            ans.append('b')

    return "".join(ans)

if __name__ == '__main__':
    a = 4 
    b = 1
    print(strWithout3a3b(a,b))
    a = 2
    b = 1
    print(strWithout3a3b(a,b))
    a = 1
    b = 3
    print(strWithout3a3b(a,b))
    a = 2
    b = 5
    print(strWithout3a3b(a,b))