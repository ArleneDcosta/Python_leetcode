from math import log
 
 
def log2(x, base):
    return int(log(x) / log(base))
 
def findOddOccuring(A):
    #since result will have only one as it is xor.
    result = 0
    for i in A:
        result = result ^ i
    #Finding the rightmost set bit.
    #Dividing the subarray for set bit
    #If both are set then only it will be set in result
    #Result will be set in x or y.
    k = log2(result & -result, 2)
    x = y = 0
    
    for i in A:
 
        if i & (1 << k):
            x = x ^ i
 
        else:
            y = y ^ i
 
    print("The odd occurring elements are", x, "and", y)
 
 

 
A = [4, 3, 6, 2, 4, 2, 3, 4, 3, 3]
findOddOccuring(A)
