from typing import List
from collections import defaultdict

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x:(-x[0],x[1]))
    print(people)

    result = []
    for p in people:
        result.insert(p[1],p)
        print(result)

    return result
if __name__ == '__main__':
    reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])

