# Python3 program to find a triplet

# returns true if there is triplet
# with sum equal to 'sum' present
# in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):

    # Sort the elements
    A.sort()
    print A
    # Now fix the first element
    # one by one and find the
    # other two elements
    for i in range(0, arr_size-2):
 
        l = i + 1
        
        # index of the last element
        r = arr_size-1
        while (l < r):
        
            if( A[i] + A[l] + A[r] == sum):
                print("Triplet is "+str(A[i])+
                    ', '+ str(A[l])+ ', '+ str(A[r]));
                l+=1
                #return True
            
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1

    # If we reach here, then
    # no triplet was found
    #return False

# Driver program to test above function
A = [2,7,4,0,9,5,1,3]
sum = 6
print(sum)
arr_size = len(A)

find3Numbers(A, arr_size, sum)

# This is contributed by Smitha Dinesh Semwal
