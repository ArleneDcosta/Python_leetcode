from typing import List

def checkdiff(diff,queries):
    dp = [0]* len(queries)
    currentlist = []
    for i in range(0,2):
        if '+' in queries[i]:
            currentlist.append(int(queries[i].lstrip("+")))
        if '-' in queries:
            no = int(queries[i].lstrip("-"))
            currentlist.remove(no)

    for i in range(2,len(queries)):
        no = int(queries[i].lstrip("+"))
        if '+' in queries[i]:
            no = int(queries[i].lstrip("+"))
            currentlist.append(no)
        if '-' in queries[i]:
            no = int(queries[i].lstrip("-"))
            currentlist.remove(no)
        res = 0
        for no in currentlist:
            if no-diff in currentlist and no+diff in currentlist:
                res += 1
        dp[i] = res

    return dp

if __name__ == '__main__':
    # diff = 2
    # queries = ["+2", "+4", "+6"]


    # diff = 1
    # queries = ["+1", "+2", "+3", "-2", "+4"]

    print("INSDIE")
    diff = 3
    queries = ["+3", "+6", "+9", "+12", "-9"]
    print(checkdiff(diff,queries))

    diff = 5
    queries = ["-5", "-10"]



