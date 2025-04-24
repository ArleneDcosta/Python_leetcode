from collections import Counter

def reverse_number(no):
    if no == 0:
        return 0
    rev = 0
    while no > 0:
        rev = rev * 10 + no % 10
        no //= 10
    return rev

def solution(arr):
    flippedarr = []
    diffs = []
    for no in arr:
        rev = reverse_number(no)
        flippedarr.append(rev)
        diffs.append(no - rev)

    counter = Counter(diffs)
    
    res = 0
    for cnt in counter.values():
        res += cnt * (cnt + 1) // 2  # includes i == j
    
    return res
