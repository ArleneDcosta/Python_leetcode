from datetime import datetime,timedelta
from heapq import heappush,heappop
import math


def solution(balances, requests):
    pendingcashbacks = {}
    ts = []
    for request in requests:
        transaction,u_timestamp,acc,amt = request.split()
        u_timestamp = int(u_timestamp)
        acc = int(acc)
        amt = int(amt)
        tstime = datetime.fromtimestamp(u_timestamp)
        if ts:
            highest_ts = heappop(ts)
            while(highest_ts is not None and tstime > highest_ts ):
                balances[pendingcashbacks[highest_ts][0]] += math.floor(0.02 * pendingcashbacks[highest_ts][1])
                if ts:
                    highest_ts = heappop(ts)
                else:
                    highest_ts = None
            if highest_ts is not None and tstime < highest_ts:
                heappush(ts,highest_ts)
        if transaction == 'deposit':
            balances[acc-1] += amt
        else:
            cashbacktime = tstime + timedelta(hours=24)
            pendingcashbacks[cashbacktime] = [acc - 1,amt]
            heappush(ts,cashbacktime)
            if balances[acc - 1] == 0:
                return balances
            else:
                balances[acc - 1] -= amt
    return balances

if __name__ == '__main__':
    balances = [1000,1500]
    requests = ["withdraw 1613327630 2 480","withdraw 1613327644 2 800","withdraw 1614105244 1 100", "deposit 1614108844 2 200","withdraw 1614108845 2 150"]
    print(solution(balances,requests))