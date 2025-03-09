from collections import defaultdict

def findCelebrity(graph):
    relationship = defaultdict(list)

    for i in range(0,len(graph)):
        for j in range(0,len(graph[0])):
            if graph[i][j] == 1 and i!=j:
                relationship[i].append(j)

    for i in range(0,len(graph)):
        if i not in relationship:
            return i

    return -1


if __name__ == '__main__':
    
    graph = [[1,1,0],
  [0,1,0],
  [1,1,1]]
    print(findCelebrity(graph))

    graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
    ]
    print(findCelebrity(graph))

    graph  = [ [0, 0, 1, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 0],
               [0, 0, 1, 0] ]
    print(findCelebrity(graph))