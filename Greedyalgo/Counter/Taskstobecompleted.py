from typing import List
from collections import Counter

def leastInterval(tasks: List[str], n: int) -> int:
    counter = Counter(tasks)
    sorted_count = sorted(list(counter.values()))
    print(counter,sorted_count)
    max_count = sorted_count.pop()
    idle_space = (max_count - 1) * n
    while sorted_count:
        idle_space -= min(sorted_count.pop(),max_count - 1)
        if idle_space <= 0:
            return len(tasks)

    n = len(tasks)
    return idle_space + n

if __name__ == '__main__':
    print(leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
    print(leastInterval(["A", "A", "A", "B", "B", "B"], 0))