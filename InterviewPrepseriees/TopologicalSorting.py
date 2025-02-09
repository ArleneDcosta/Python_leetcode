from collections import defaultdict

class DependencyGraph:
    def __init__(self):
        self.graph = defaultdict(list)  
        self.visited = set()            
        self.in_progress = set()        
        self.stack = []                 

    def add_dependency(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node):
        if node in self.visited:  
            return
        if node in self.in_progress:  
            raise ValueError(f"Circular dependency detected at {node}!")

        self.in_progress.add(node)  
        for neighbor in self.graph[node]:
            self.dfs(neighbor)  

        self.in_progress.remove(node)  
        self.visited.add(node)
        self.stack.append(node)  

    def get_execution_order(self):
        for node in list(self.graph.keys()):
            if node not in self.visited:
                self.dfs(node)

        return self.stack[::-1] 


graph = DependencyGraph()

graph.add_dependency("Table", "View")        
graph.add_dependency("View", "StoredProc")   
graph.add_dependency("Table", "StoredProc")  


execution_order = graph.get_execution_order()
print("Execution Order:", execution_order)
