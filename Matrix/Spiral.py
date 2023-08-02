def spiralOrder(matrix):
    result = []
    sRow, eRow = 0, len(matrix) - 1
    sCol, eCol = 0, len(matrix[0]) - 1

    while sRow <= eRow and sCol <= eCol:

        for col in range(sCol, eCol + 1):
            result.append(matrix[sRow][col])

        for rows in range(sRow + 1, eRow + 1):
            result.append(matrix[rows][eCol])

        for col in reversed(range(sCol, eCol)):
            if sRow == eRow:
                break
            result.append(matrix[eRow][col])

        for rows in reversed(range(sRow + 1, eRow)):
            if sCol == eCol:
                break
            result.append(matrix[rows][sCol])
        sRow += 1
        eRow -= 1
        sCol += 1
        eCol -= 1

    return result

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
