from collections import defaultdict, deque

def transformStringToAnotherCheck(str1:str,str2:str) -> bool:
    if len(str1) != len(str2): 
        return False
    
    for i in range(0,len(str1) - 1):
        if str1[i] == str1[i+1] and str2[i] != str2[i+1]:
            return False

    g = dict()

    for i in range(len(str1)):
        if str1[i] in g:
            if g[str1[i]] != str2[i]:
                return False  
        else:
            g[str1[i]] = str2[i]

    total_nodes = len(set(str1 + str2))
    in_degree = defaultdict(int)

    for u in g:
        if u not in in_degree:
            in_degree[u] = 0
        in_degree[g[u]] += 1

    queue = deque([node for node in in_degree if in_degree[node] == 0])
    visited = 0

    while queue:
        current_node = queue.popleft()
        visited += 1
        neighbor = g.get(current_node)
        if neighbor:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited == total_nodes

if __name__ == '__main__':
    str1 = "aabcc"
    str2 = "ccdee"
    print(transformStringToAnotherCheck(str1,str2))

    str1 = "leetcode"
    str2 = "codeleet"
    print(transformStringToAnotherCheck(str1,str2))

    str1 = "ab"
    str2 = "ba"
    print(transformStringToAnotherCheck(str1,str2))

    str1 = "abdffg"
    str2 = "cqrtsw"
    print(transformStringToAnotherCheck(str1,str2))

    str1 = "abcdefghijklmnopqrstuvwxyz"
    str2 = "bcdefghijklmnopqrstuvwxyza"
    print(transformStringToAnotherCheck(str1,str2))