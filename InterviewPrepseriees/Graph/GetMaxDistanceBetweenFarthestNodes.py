from collections import defaultdict, deque

def getMaxTime(g_nodes, g_from, g_to):
    graph = defaultdict(list)
    for start_node, end_node in zip(g_from, g_to):
        graph[start_node].append(end_node)
        graph[end_node].append(start_node)
        
    def bfs(start):
        visited = [-1] * (g_nodes + 1) 
        visited[start] = 0
        queue = deque([start])
        farthest_node = start
        max_distance = 0

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == -1: 
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)

                    if visited[neighbor] > max_distance:
                        max_distance = visited[neighbor]
                        farthest_node = neighbor

        return farthest_node, max_distance

    farthest_node, _ = bfs(1)
    
    _, max_distance = bfs(farthest_node)

    return max_distance

