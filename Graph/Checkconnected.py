# Python3 implementation of the approach
N = 5

# To keep correct and reverse direction
gr1 = {}; gr2 = {}

vis1 = [0] * N; vis2 = [0] * N

# Function to add edges
def Add_edge(u, v) :
    if u not in gr1 :
        gr1[u] = []
        
    if v not in gr2 :
        gr2[v] = []
        
    gr1[u].append(v)
    gr2[v].append(u)
    print(gr1)
    print(gr2)
# DFS function
def dfs1(x) :
    vis1[x] = True;
    if x not in gr1 :
        gr1[x] = {};
        
    for i in gr1[x] :
        if (not vis1[i]) :
            dfs1(i)
    #print(gr1)
# DFS function
def dfs2(x) :
    vis2[x] = True;
    if x not in gr2 :
        gr2[x] = {};
        
    for i in gr2[x] :
        if (not vis2[i]) :
            dfs2(i);
    print(gr2)
def Is_Connected(n) :
    global vis1;
    global vis2;
    
    # Call for correct direction
    vis1 = [False] * len(vis1);
    dfs1(1);
    
    # Call for reverse direction
    vis2 = [False] * len(vis2);
    dfs2(1);
    print(vis1,vis2)
    for i in range(1, n + 1) :
    # If any vertex it not visited in any direction
    # Then graph is not connected
        if (not vis1[i] and not vis2[i]) :
            return False;
         
    # If graph is connected
    return True;

# Driver code
if __name__ == "__main__" :
    n = 4;
    #both the directions are considered for strong connections
    # Add edges
    Add_edge(1, 2);
    Add_edge(1, 3);
    Add_edge(2, 3);
    Add_edge(3, 4);

    # Function call
    if (Is_Connected(n)) :
        print("Yes");
    else :
        print("No");

# This code is contributed by AnkitRai01
