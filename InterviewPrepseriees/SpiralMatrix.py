from typing import List 

def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    startrow = 0
    startcol = 0
    endrow = len(matrix) - 1
    endcol = len(matrix[0]) - 1

    while(startrow <= endrow and startcol <= endcol):
        #print('Startrow',startrow,startcol,endrow,endcol,result)
        if startrow <= endrow:
            
            for i in range(startcol,endcol+1):
                result.append(matrix[startrow][i])

            startrow += 1

        #print('endrow',startrow,startcol,endrow,endcol,result)
        if startrow <= endrow:
            for i in range(startrow,endrow + 1):
                result.append(matrix[i][endcol])
            endcol -= 1

        #print('startcol',startrow,startcol,endrow,endcol,result)
        if endrow >= startrow:
            for i in range(endcol,startcol - 1,-1):
                result.append(matrix[endrow][i])

            endrow -= 1

        #print('endcol',startrow,startcol,endrow,endcol,result)
        if endrow > startrow and endcol >= startcol:
            for i in range(endrow,startrow -1,-1):
                result.append(matrix[i][startcol])

            startcol += 1

    return result

if __name__ == '__main__':
    print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(spiralOrder([[3],[2]]))
    print(spiralOrder(matrix =[[2,5,8],[4,0,-1]]))
    print(spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]))
    print(spiralOrder(matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]))
