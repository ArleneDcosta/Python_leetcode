from typing import List
#similiar to MST
class DSU:
    def __init__(self,n):
        self.parents = list(range(n))
        self.edges = 0

    def find(self,x):
        #Ancester value(The first node)
        print("Inside find ",x,self.parents)
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]

    def union(self,x,y):
        r1 = self.find(x)
        r2 = self.find(y)
        print("Inside union", r1,r2)
        if r1 != r2:
            # U are drawing an edge
            self.parents[r2] = r1
            print("checking update",self.parents)
            self.edges += 1
            # Dont remove edge
            return 0
        else:
            # Remove edge
            return 1

def maxNumEdgesToRemove(n: int, edges: List[List[int]]) -> int:
    alice = DSU(n+1) # Convert to 1 based system
    bob = DSU(n+1)
    ans = 0
    for t,u,v in edges:
        if t == 3:
            ans += alice.union(u,v)
            bob.union(u,v)
            print("1 iteration done")

    for t,u,v in edges:
        if t == 1:
            ans += alice.union(u,v)
        if t == 2:
            ans += bob.union(u,v)

    return ans if alice.edges == bob.edges == n - 1 else -1

###BFS and DFS is not advisable because traversal is difficult

if __name__ == '__main__':
    #print(maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))