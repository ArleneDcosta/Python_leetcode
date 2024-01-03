import math
def rotate(matrix):
    last_row = len(matrix)
    last_col = len(matrix[0])
    k = 0
    l = 0
    totalele = math.ceil((len(matrix) * len(matrix[0]))/ 2)
    finalrow = finalcol = 0
    count  = 0
    while(k <= last_row and l <= last_col):
        if count == totalele:
            break
        for i in range(k,last_row,2):
            count+=1
            finalrow = i
            finalcol = l
            #print('first',finalrow, finalcol, count)
        l+=1

        if count == totalele:
            break
        # Here + 1 because of two ahead
        for i in range(l+1 ,last_col,2):
            count+=1
            finalrow = last_row - 1
            finalcol = i
            #print('second',finalrow, finalcol, count)
        last_row -=1

        if count == totalele:
            break

        if(k < last_row):
            for i in range(last_row - 2,k-1,-2):
                count+=1
                finalrow = i
                finalcol = last_col - 1
               # print('third',finalrow, finalcol, count)
            last_col -=1

        if count == totalele:
            break

        if(l < last_col):
            for i in range(last_col - 2,l - 1,-2):
                count+=1
                finalrow = k
                finalcol = i
                #print('fourth',finalrow, finalcol, count)
            k += 1
    return matrix[finalrow][finalcol]

if __name__ == '__main__':
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))