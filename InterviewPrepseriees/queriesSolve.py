def checkPairs(a,b,tgt):
    cnt = 0
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i] + b[j] == tgt:
                cnt += 1
    return cnt


def queriesSolve(a,b,queries):
    res = []
    for query in queries:
        if len(query) == 2:
            if query[0] == 1:
                res.append(checkPairs(a,b,query[1]))
        elif len(query) == 3:
            if query[0] == 0:
                b[query[1]] += query[2]

    return res


if __name__ == '__main__':
    a = [1,2,3]
    b = [1,4]
    queries = [[1,5],[0,0,2],[1,5]]
    print(queriesSolve(a,b,queries))