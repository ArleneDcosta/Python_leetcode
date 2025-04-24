from typing import List
from heapq import heappop, heappush

def bagOfTokensScore(tokens: List[int], power: int) -> int:
    tokens.sort()   
    s = 0                 
    maxi = 0              
    l, r = 0, len(tokens) - 1  
    
    while l <= r:
        if power >= tokens[l]:   
            power -= tokens[l]   
            s += 1               
            l += 1               
            maxi = max(maxi, s) 
        elif s > 0:                
            power += tokens[r]   
            s -= 1              
            r -= 1               
        else:
            break
    return maxi 

if __name__ == '__main__':
    tokens = [100,200,300,400]
    power = 200
    print(bagOfTokensScore(tokens,power))