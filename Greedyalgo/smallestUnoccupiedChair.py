from heapq import heapify,heappop,heappush
def smallestUnoccupiedChair(times,targetFriend):
    times = [(a,l,i) for i,(a,l) in enumerate(times)]
    times.sort()

    availableChairs = list(range(10)) #chair index
    heapify(availableChairs)
    print(times,availableChairs)
    usedChairs = [] #(leaving time,chair index)

    for a,l,i in times:
        print(usedChairs)
        # free all used chairs whose leaving time <= a
        while usedChairs and usedChairs[0][0] <= a:
            _,idx = heappop(usedChairs)
            heappush(availableChairs,idx)
            print(_, idx,availableChairs)
        cur = heappop(availableChairs)
        print('CUR:',cur,(a,l,i),availableChairs)
        if i == targetFriend:
            return cur
        heappush(usedChairs,(l,cur))

if __name__ == '__main__':
    print(smallestUnoccupiedChair([[3,10],[6,8],[1,5]],1))
