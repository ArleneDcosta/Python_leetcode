
from typing import List
from collections import Counter,defaultdict

def numPairsDivisibleBy60(time: List[int]) -> int:
        # res = 0
        # visited = defaultdict(int)
        # exact60 = []
        # for ele in time:
        #     if ele < 60:
        #         modres = 60 - ele
        #         print(ele,modres)
        #     elif ele > 60:
        #         modres = ele % 60
        #         print(ele,modres)
        #     else:
        #         modres = 0
        #         exact60.append(ele)

        #     if modres in time and modres != ele and visited[modres] == 0 and modres!=0 :
        #         res += 1
        #         visited[ele] = 1
        # res += len(exact60)
        # return res
        d = {}
        pairs = 0
        
        for t in time:
            numMod = t % 60
            
            if numMod == 0:
                if 0 in d:
                    pairs += d[0]
            elif (60 - numMod) in d:
                pairs += d[60 - numMod]
                
            if numMod in d:
                d[numMod] += 1
            else:
                d[numMod] = 1
                
        return pairs

if __name__ == '__main__':
     time =  [30,20,150,100,40,20]
     print(numPairsDivisibleBy60(time))

     time =  [60,60,60]
     print(numPairsDivisibleBy60(time))