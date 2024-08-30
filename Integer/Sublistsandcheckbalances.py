
from typing import List
import time
from collections import defaultdict

def sublistcheckbalancenonoptimized(capacity):
    start_time = time.time()
    ans = 0
    res = []
    for i in range(0,len(capacity)):
        current_list = []
        for j in range(i+3,len(capacity)+1):
            res.append(capacity[i:j])

    for ele in res:
        if ele[0] == ele[len(ele)-1] and ele[0] == sum(ele[1:len(ele)-1]):
            ans += 1
    end_time = time.time()
    print(f"Total time elapsed is {end_time - start_time}")
    return ans

def sublistcheckbalanceoptimized(capacity):
    start_time = time.time()
    first = defaultdict(lambda: 0)
    last = defaultdict(lambda: 0)
    mid = defaultdict(lambda:[])

    n = len(capacity)
    pr = [None] * n
    pr[0] = capacity[0]
    first[capacity[0]] = 1
    last[capacity[0]] = 1

    for i in range(1, n):

        # Build prefix sum array
        pr[i] = pr[i - 1] + capacity[i]

        # If the value hasn't been encountered before,
        # It is the first occurrence
        if first[capacity[i]] == 0:
            first[capacity[i]] = i + 1

        # Keep updating the last occurrence
        last[capacity[i]] = i + 1
    print(f"Sum is {pr}")
    for i in range(0,n):
        start = first[capacity[i]]
        end = last[capacity[i]]
        if i + 1 not in (start, end):
            mid[capacity[i]].append(i+1)

    ans = 0
    res = []

    # Find the maximum sum with same first and last value
    for i in range(0, n):
        start = first[capacity[i]]
        end = last[capacity[i]]


        if (capacity[i],pr[end - 2] - pr[start - 1]) not in res and capacity[i] == pr[end - 2] - pr[start - 1]:
            ans += 1
            res.append((capacity[i],pr[end - 2] - pr[start - 1]))

        if capacity[i] in mid and i+1 not in (start,end):
            midlist = mid[capacity[i]]
            for j in range(0,len(midlist)):
                if capacity[i] == pr[midlist[j] - 2] - pr[start - 1]:
                    ans += 1
                if capacity[i] == pr[end - 2] - pr[midlist[j] - 1]:
                    ans += 1
                for k in range(j+1,len(midlist)):
                    if capacity[i] == pr[midlist[k] - 2] - pr[midlist[j] - 1]:
                        ans += 1
            mid[capacity[i]] = []
    end_time = time.time()
    print(f"Total time elapsed in second method is {end_time - start_time}")
    return ans

def sublistcheckbalanceoptimizednew(capacity):
    start_time = time.time()
    n = len(capacity)
    pr = [None] * n
    pr[0] = capacity[0]
    last_index = {}
    ans = 0

    for i in range(1, n):
        # Build prefix sum array
        pr[i] = pr[i - 1] + capacity[i]

    for i in range(0,n):
        if i > 1:
            if capacity[i] in last_index and sum(capacity[last_index[capacity[i]]+1:i]) == capacity[i] :
                ans += 1
            elif capacity[i] == capacity[i-2] and capacity[i-1] == capacity[i]:
                ans += 1
        last_index[capacity[i]] = i


    end_time = time.time()
    print(f"Total time elapsed in third method is {end_time - start_time}")
    return ans


if __name__ == '__main__':
    print(sublistcheckbalancenonoptimized([1]*2000))

    print(sublistcheckbalanceoptimized(
        [1]*2000))

    print(sublistcheckbalanceoptimizednew([1]*2000))

    # print(sublistcheckbalanceoptimizednew([2,2,2,2,2]))
    # print(sublistcheckbalanceoptimizednew([9,3,3,3,9]))