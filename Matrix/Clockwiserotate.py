def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    #Reversing the array
    for i in range(0,cols):
        for j in range(0,int(rows/2)):
            matrix[rows-j-1][i],matrix[j][i] = matrix[j][i],matrix[rows-j-1][i]
    
    #Transpose of the matrix
    for i in range(0,rows):
        for j in range(i+1,cols):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            #print(matrix)
    return(matrix)
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
