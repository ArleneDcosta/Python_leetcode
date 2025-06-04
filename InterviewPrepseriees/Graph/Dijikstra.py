import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()
    
    heap = [(0, start)]
    
    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited: # This is essentially needed if a shorter path was added afer the same node was longer 
            # and present
            continue
        visited.add(current_node)
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances
