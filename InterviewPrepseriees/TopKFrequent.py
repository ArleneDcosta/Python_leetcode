from typing import List
from collections import Counter
import heapq
import collections
import functools

def topKFrequent(words: List[str], k: int) -> List[str]:
    c = Counter(words)
    resVal = []
    for ele in c.keys():
        resVal.append((ele,c[ele]))
    resVal = sorted(resVal)
    resVal = sorted(resVal, key = lambda x:x[1],reverse = True)
    res = [ key for key,val in resVal[0:k] ]
    print(res)

@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution(object):
    def topKFrequent(self, words, k):
        counts = collections.Counter(words)   
        
        freqs = []
        heapq.heapify(freqs)
        for word, count in counts.items():
            heapq.heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs)[1])
        return res[::-1]

if __name__ == '__main__':
    topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4)
    topKFrequent(["i","love","leetcode","i","love","coding"],2)