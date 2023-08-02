# Python 3 program to reverse every
# sub-array formed by consecutive k
# elements

# Function to reverse every sub-array
# formed by consecutive k elements
def reverse(arr, n, k):
    i = 0
    
    while(i<n):
    
        left = i

        # To handle case when k is not
        # multiple of n
        right = min(i + k - 1, n - 1)

        # Reverse the sub-array [left, right]
        while (left < right):
            
            arr[left], arr[right] = arr[right], arr[left]
            left+= 1;
            right-=1
        i+= k
      
# Driver code
arr = [1, 2, 3, 4, 5, 6,
                7, 8]

k = 3
n = len(arr)
reverse(arr, n, k)

for i in range(0, n):
        print(arr[i], end =" ")
        
# This code is contributed by Smitha Dinesh Semwal
