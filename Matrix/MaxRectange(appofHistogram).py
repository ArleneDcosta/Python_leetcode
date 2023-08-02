def maximalRectangle(matrix):
    rows, cols = len(matrix), len(matrix[0])
        '''This block updates the matrix. Each cell of every row stores height of the building(consecutive 1's from that cell to above cells).'''
        
    for i in range( rows):
        for j in range(cols):
            matrix[i][j] = int(matrix[i][j])
            if i>0 and matrix[i][j] ==1 and matrix[i-1][j]!= 0:
                matrix[i][j] =  1 +  matrix[i-1][j] 
        print(matrix[i])
              
    '''Here we perform the same operation as for Largest area of histogram, for every row, considering each row as array of heights of the histogram at that row level'''
    maxArea = 0
    for row in matrix:
        row.append(0)
        stack = [-1]
        i = 0
        for i, height in enumerate(row):
            while(height<row[stack[-1]]):
                h = row[stack.pop()]
                width = i - 1 - stack[-1]
                maxArea = max(maxArea, h*width)
            stack.append(i)
    return maxArea
