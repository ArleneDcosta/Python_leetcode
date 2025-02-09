from typing import List

def carPooling(trips: List[List[int]], capacity: int) -> bool:
    trips.sort(key = lambda x : x[1])
    max_time = -10000
    for ele in trips:
        max_time = max(max_time, ele[2])
       

    curr_capacity_list = [0] * (max_time + 1)
    for trip in trips:
        for i in range(trip[1],trip[2]):
            curr_capacity_list[i] = curr_capacity_list[i] + trip[0]
            if curr_capacity_list[i] > capacity:
                return False
             

    return True

if __name__ == '__main__':
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    print(carPooling(trips,capacity))

    trips = [[2,1,5],[3,3,7]]
    capacity = 5
    print(carPooling(trips,capacity))

    trips = [[2,1,5],[3,5,7]]
    capacity = 3
    print(carPooling(trips,capacity))

    trips = [[2,2,6],[2,4,7],[8,6,7]]
    capacity = 11
    print(carPooling(trips,capacity))