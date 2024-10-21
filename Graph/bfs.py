
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}
#Visited can also be used as a distance
dist = {} # List for visited nodes.
queue = []     #Initialize a queue
for node in graph:
    dist[node] = 100000000

def bfs(visited, graph, node): #function for BFS
  visited[node] = 0
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m,visited[m])
    for neighbour in graph[m]:
      if visited[neighbour] == 100000000:
        visited[neighbour] = visited[m] + 1
        queue.append(neighbour)

# Driver Code
if __name__ == '__main__':
  print("Following is the Breadth-First Search")
  bfs(dist, graph, '5')    # function calling