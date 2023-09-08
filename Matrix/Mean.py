

def calculatemeanimage(matrix,radius):
    def get_neighbouring_elements(matrix,d,i,j):
        cnt = 0
        res = 0
        for ele in d:
            newrow, newcol = i + ele[0], j + ele[1]
            if 0 <= newrow < rows and 0 <= newcol < cols:
                if newrow == i and newcol ==j :
                    pass
                else:
                    cnt += 1
                    print('inside',matrix[newrow][newcol],i,j,newrow,newcol)
                    res += matrix[newrow][newcol]
        return res//cnt

    rows =  len(matrix)
    cols = len(matrix[0])

    d = []
    for i in range(1,radius + 1):
        [d.append(l) for l in ([0,i],[0,-i],[i,0],[-i,0],[i,i],[-i,-i],[-i,i],[i,-i])]
    print(d)

    updatematrix = [[0] * cols for _ in range(rows)]
    print(updatematrix)

    for i in range(rows):
        for j in range(cols):
            print("Outside",i,j)
            res = get_neighbouring_elements(matrix,d,i,j)
            updatematrix[i][j] = (matrix[i][j] + res) // 2

    return updatematrix
if __name__ == '__main__':
    print(calculatemeanimage([[9,3],[6,0]],1))