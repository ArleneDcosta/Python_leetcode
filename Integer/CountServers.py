def countServers(grid):
    row={}
    col={}
    res=0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print i,j
            if grid[i][j]==1:
                if i not in row:
                    row[i]=[j]
                else:
                    row[i].append(j)
                if j not in col:
                    col[j]=[i]
                else:
                    col[j].append(i)
    print row,col
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                if (i in row and len(row[i])>=2) or (j in col and len(col[j])>=2):
                    res+=1
    return res

print countServers(([1,0],[1,1]))
