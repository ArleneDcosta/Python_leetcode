from typing import List


#problem can be solved using Knapsack method but depending on the constraints in the leetcode problem
# decisions can be taken

#farthest place u can go at a particular location with
# j = different variations of fuel(constraint m is 100) cannot be used because it will give memory error because
# of contraints , hence n will be the no of steps and i = no of elements[Weight]
#Fuel is the profit value as in Knapsack, target = M
def minRefuelStops(target: int, startFuel: int, stations: List[List[int]]) -> int:
    n = len(stations)
    dp = [[0] * (n+1) for _ in range(n+1)]

    #base case move without refuelling
    for i in range(n+1):
        dp[i][0] = startFuel
    #Here j is considered
    for i in range(n+1):
        for j in range(1,i+1):
            #Prev value will always be retained as the current value exceeds the required cond or is lesser or
            # current station will not be refueled/use the same as prev station or weight / current weight will not be considered4
            print(i-1,j)
            dp[i][j] = dp[i-1][j]
            # j - 1 because we always update current + 1
            #Also stations[i - 1] is because of dp always updated to + 1
            # Refuel at current station
            if dp[i-1][j-1] >= stations[i-1][0]:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1] + stations[i-1][1])

    for i in range(n+1):
        if dp[n][i] >= target:
            return i
    return -1

if __name__ == '__main__':
    minRefuelStops(target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]])
