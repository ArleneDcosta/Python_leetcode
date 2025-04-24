from typing import List
from heapq import heapify, heappop,heappush
from collections import Counter

def findContentChildrenwrong(g: List[int], s: List[int]) -> int:
    content = 0
    g.sort()
    heapify(s)
    for child in g:
        if s:
            current_cookie = heappop(s)
            if current_cookie > child:
                content += 1
                heappush(s, current_cookie - child)

            elif current_cookie == child:
                content += 1
            else:
                return content
        else:
            return content
    return content

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    content_children = 0
    cookie_index = 0
    while cookie_index < len(s) and content_children < len(g):
        if s[cookie_index] >= g[content_children]:
            content_children += 1
        cookie_index += 1
    return content_children

if __name__ == '__main__':
    g = [1,2,3]
    s = [1,1]
    print(findContentChildren(g,s))

    g = [1,2]
    s = [1,2,3]
    print(findContentChildren(g,s))