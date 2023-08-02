import collections
def numBusesToDestination(routes, S, T):
    if S == T: return 0
    routes = map(set, routes)
    print 'routes',routes
    graph = collections.defaultdict(set)
    for i, r1 in enumerate(routes):
        print i,r1
        for j in xrange(i+1, len(routes)):
            r2 = routes[j]
            if any(r in r2 for r in r1):
                graph[i].add(j)
                graph[j].add(i)
    print 'graph',graph  
    seen, targets = set(), set()
    for node, route in enumerate(routes):
        if S in route: seen.add(node)
        if T in route: targets.add(node)
    print 'seen',seen,'targets',targets
    queue = [(node, 1) for node in seen]
    print 'queue',queue
    for node, depth in queue:
        if node in targets: return depth
        for nei in graph[node]:
            if nei not in seen:
                print nei,'nei'
                seen.add(nei)
                queue.append  ((nei, depth+1))
    return -1
print numBusesToDestination([[1,2,7],[3,6,7]],1,6)
