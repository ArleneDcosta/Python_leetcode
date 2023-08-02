def gray_code(n):
# logic is:
# for 1- [0,1]
# for 2 - [0,1,3,2] - not that first half of array is same as for n=1 addition for i=2 is (2**1)+1 => 3, (2**1)+0 => 2
# that is [0,1,1,0] => first half of array + concatenate reverse part of array and add powers of 2 to it  
    oldArr = [0,1]
    i = 1
    while i< n:
	# add old array
        newArr = list(oldArr)
        # now add bit value to old reversed values
        for j in range(len(oldArr)-1,-1,-1):
            print(newArr,i,j)
            newArr.append((2**i)+oldArr[j])
        oldArr = newArr
        i+=1
    return oldArr



print(gray_code(4))
