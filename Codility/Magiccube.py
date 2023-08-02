def isMagicSquare(a, x1, y1,x2,y2):
    size = x2 - x1 + 1 
    diagonalSum = a[x1][y1]
    secondDiagonalSum = a[x1][y2]
    magicSquareSize = 1
    index =0
    row = x1
    column = y1
    end = y2-1
    while(index < size):
        if (row != x2)  
            diagonalSum = diagonalSum + a[row + 1][column + 1]
            secondDiagonalSum = secondDiagonalSum + a[row + 1][end]
        row+=1
        column+=1
        end-=1
        index+=1
            
        

    if(diagonalSum == secondDiagonalSum):
        rowSum = [ [ 0 for i in range(size) ] for j in range(size) ]
        colSum = [ [ 0 for i in range(size) ] for j in range(size) ]

    row=0
    col=0
    xIndex=x1
    yIndex=y1
    while(row < size and col < size):
        rowSum[row][0] = a[xIndex][y1]
        colSum[0][col] = a[x1][yIndex]
        row+=1
        col+=1
        xIndex+=1
        yIndex+=1
    xIndex=0
    row=x1
    
    while(xIndex < size; row++, xIndex++):
        yIndex=1
        col=y1+1
        while(yIndex < size):
            rowSum[xIndex][yIndex] = rowSum[xIndex][yIndex-1] + a[row][col]
            if(diagonalSum != rowSum[xIndex][size-1]): return -1
            col+=1
            yIndex+=1
        yIndex=0
        col=y1
        while(yIndex < size):
            xIndex=1
            row=x1+1
            while(xIndex < size):
                    colSum[xIndex][yIndex] = colSum[xIndex-1][yIndex] + a[row][col]

                if(diagonalSum != colSum[size-1][yIndex]): return -1;
                row+=1
                xIndex+=1
            yIndex+=1
            col+=1

            #System.out.println("(x1,y1) => (" + x1 + "," + y1 + ") (x2,y2) => (" + x2 + "," + y2 + ")");
        magicSquareSize = size
        row+=1
        xIndex+=1
    return magicSquareSize
    
def solution(a):
    if(a == null or a.length == 0):
        return 0

    maxMagicSquareSize = 1
    rowSize = a.length
    colSize = a[0].length

    if(rowSize == 1 || colSize == 1):
        return maxMagicSquareSize

    row=0
    for row in range(0,rowSize - 1):
        for col in range(0,colSize):
            xOffset = row + 1
             yOffset = col + 1
            while xOffset < rowSize and yOffset < colSize):
                currentSubMatrixSize = xOffset - row + 1
                    // if maxMagicSquareSize >= currentSubMatrixSize, then skip checking of this subMatrix
                    if(maxMagicSquareSize >= (xOffset - row + 1))
                        continue;
                    maxMagicSquareSize = Math.max(isMagicSquare(a, row, col, xOffset, yOffset), maxMagicSquareSize);
                }
            }
        }
        return maxMagicSquareSize;
    }
