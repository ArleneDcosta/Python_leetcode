def summ(a):
    row=len(a)
    col=len(a[0])
    if row ==col:
        #print a
        tot = row *(row * row + 1)/ 2
        colsum = [sum(i) for i in zip(*a)]
        #print colsum
        if len(list(set(colsum)))!=1:
            return 0
        rowsum = []
        for ele in a:
            rowsum.append(sum(ele))
        if len(list(set(rowsum)))!=1:
            return 0
        #print rowsum,colsum
        diagonal1 =[a[i][i] for i in xrange(len(a))]
        diagonal2 =[a[i][len(a)-1-i] for i in xrange(len(a))]
        if sum(diagonal1)!=sum(diagonal2):
            return 0
        elif sum(diagonal1)==tot:
            return row
    return 0
            
    
def getsubgrid(x1, y1, x2, y2, grid):
    return [item[x1:x2] for item in grid[y1:y2]]
def solve(grid):
    n=len(grid)
    m=len(grid[0])
    l=len(grid)
    while(l>1):
        #print(l)
        for i in range(n-l+1):
            for j in range(m-l+1):
                n=summ(getsubgrid(i,j,i+l,j+l,grid))
                if n:
                    return n
        l-=1
    return 1
            
print solve([[4,9,2],[3,5,7],[8,1,6]])
  





