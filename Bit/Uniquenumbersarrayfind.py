def UniqueNumbers2(arr, n):

    sums = 0

    for i in range(0, n):
    
    # Xor all the elements of the array
    # all the elements occuring twice will
    # cancel out each other remaining
    # two unnique numbers will be xored
        sums = (sums ^ arr[i])
    
# Bitwise & the sum with it's 2's Complement
# Bitwise & will give us the sum containing
# only the rightmost set bit
    sums = (sums & -sums)

# sum1 and sum2 will contains 2 unique
# elements elements initialized with 0 box
# number xored with 0 is number itself
    sum1 = 0
    sum2 = 0
'''
Approach : 
Step 1: Xor all the elements of the array into a variable sum thus all the elements present twice in an array will get removed as for example, 4 = 100 and if 4 xor 4 => 100 xor 100 thus answer will be 000. 
Step 2: Thus in the sum the final answer will be 3 xor 5 as both 2 and 4 are xor with itself giving 0, therefore sum = 011 xor 101 i.e sum = 110 = 6. 
Step 3: Now we will take 2s Complement of sum i.e (-sum) = 010. 
Step 4: Now bitwise And the 2s of sum with the sum i.e 110 & 010 gives the answer 010 (Aim for bitwise & is that we want to get a number that contains only the rightmost set bit of the sum). 
Step 5: bitwise & all the elements of the array with this obtained sum, 2 = 010 & 010 = 2, 3 = 011 & 010 = 010 , 4 = 100 & 010 = 000, 5 = 101 & 010 = 000. 
Step 6: As we can see that the bitwise & of 2,3 > 0 thus they will be xor with sum1 and bitwise & of 4,5 is resulting into 0 thus they will be xor with sum2. 
Step 7: As 2 is present two times so getting xor with sum1 two times only the result 3 is being stored in it and As 4 is also present two times thus getting xor with sum2 will cancel its value and thus
only 5 will remain there.'''
# Traversing the array again
    for i in range(0, len(arr)):
    
    # Bitwise & the arr[i] with the sum
    # Two possibilities either result == 0
    # or result > 0
        if (arr[i] & sums) > 0:
    
    # If result > 0 then arr[i] xored
    # with the sum1
            sum1 = (sum1 ^ arr[i])
    
        else:
    
    # If result == 0 then arr[i]
    # xored with sum2
            sum2 = (sum2 ^ arr[i])

# Print the the two unique numbers
    print("The non-repeating elements are ",sum1 ," and ", sum2)

# Driver Code
if __name__ == "__main__":

    arr = [ 2, 3, 7, 9, 11, 2, 3, 11 ]
    n = len(arr)
    
    UniqueNumbers2(arr, n)

# This code is contributed by akhilsaini
