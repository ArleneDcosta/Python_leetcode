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
        # if count == totalele:
        #     break
        for i in range(k,last_row):
            count+=1
            finalrow = i
            finalcol = l
            print('First',matrix[i][l])
        l+=1

        for i in range(l,last_col):
            count+=1
            finalrow = last_row - 1
            finalcol = i
            print(matrix[last_row-1][i])
        last_row -=1

        # if count == totalele:
        #     break
        print(last_row,k,last_col)
        if(k < last_row):
            for i in range(last_row - 1,k,-1):
                count+=1
                finalrow = i
                finalcol = last_col - 1
                print('Third',matrix[i][last_col-1])
            last_col -=1

        # if count == totalele:
        #     break
        print(last_col)
        if(l < last_col):
            for i in range(last_col - 1,l,-1):
                count+=1
                finalrow = k
                finalcol = i
                print('Fourth',matrix[k][i])
            k += 1
    # return matrix[finalrow][finalcol]

if __name__ == '__main__':
    rotate([[1,2],[3,4]])
    # print(rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))