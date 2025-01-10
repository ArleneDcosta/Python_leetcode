from typing import List

def partitionLabels(s: str) -> List[int]:
    last_pos = {c:i for i,c in enumerate(s)}
    #print(last_pos)
    ans  = []
    start = 0
    max_stop = 0

    for i,c in enumerate(s):
        cur_stop = last_pos[c]
        max_stop = max(cur_stop , max_stop)


        if i == max_stop:
            ans.append(i - start + 1)
            start = i + 1
    return ans