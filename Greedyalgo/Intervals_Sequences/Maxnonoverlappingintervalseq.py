# Python code for the above approach
import heapq
# The main function that returns the maximum
# possible profit from given array of
# intervals
def maximum_profit(n, intervals):
    events = []
    for i in range(len(intervals)):
        events.append((intervals[i][0], (intervals[i][1], intervals[i][2])))

    pq = []

    events.sort()
    print(events)

    max_profit = 0
    for e in events:
        print("E", e)
        while pq and pq[0][0] <= e[0]:
            max_profit = pq[0][1]
            heapq.heappop(pq)

        heapq.heappush(pq, (e[1][0], max_profit + e[1][1]))
        print(pq)
    # Check again if min heap is contain
    # any elements
    while pq:
        max_profit = max(max_profit, pq[0][1])
        heapq.heappop(pq)
    # Maximum profit
    return max_profit


# Driver code
if __name__ == '__main__':
    n = 4
    #intervals = [[5, 17, 32], [10, 30, 19], [18, 49, 21], [30, 50, 50]]
    intervals = [[5, 17, 21], [10, 30, 19], [18, 49, 32], [30, 50, 50]]
    print(maximum_profit(n, intervals))