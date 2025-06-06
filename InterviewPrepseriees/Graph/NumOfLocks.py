from typing import List
from collections import deque

def openLock(deadends: List[str], target: str) -> int:
    deadends = set(deadends)
    if "0000" in deadends:
        return -1
    
    queue = deque([('0000', 0)])  
    visited = set('0000')
    
    while queue:
        current_combination, moves = queue.popleft()
        
        if current_combination == target:
            return moves
        
        for i in range(4):
            for delta in [-1, 1]:
                new_digit = (int(current_combination[i]) + delta) % 10
                new_combination = (
                    current_combination[:i] + str(new_digit) + current_combination[i+1:]
                )
                
                if new_combination not in visited and new_combination not in deadends:
                    visited.add(new_combination)
                    queue.append((new_combination, moves + 1))
    return -1



if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(openLock(deadends,target))