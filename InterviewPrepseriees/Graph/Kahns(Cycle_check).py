from collections import defaultdict, deque

def has_cycle_topo(graph):
    in_degree = defaultdict(int)
    total_nodes = len(graph)

    # Build in-degree map
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Queue of all nodes with in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])

    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If we didn't visit all nodes, there's a cycle
    return visited_count != total_nodes
