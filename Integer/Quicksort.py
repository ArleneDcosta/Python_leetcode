# Python3 implementation of QuickSort

# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, arr):
    
    # Initializing pivot's index to start
    i=start-1
    pivot = arr[end]
    
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    for j in range(start,end):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    arr[end], arr[i+1] = arr[i+1], arr[end]
    
    # Returning end pointer to divide the array into 2
    return i+1
    
# The main function that implements QuickSort
def quick_sort(start, end, arr):
    
    if (start < end):
        
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, arr)
        
        # Sort elements before partition
        # and after partition
        arr = quick_sort(start, p - 1, arr)
        arr = quick_sort(p + 1, end, arr)
    return arr
        
# Driver code
arr = [ 10, 7, 8, 9, 1, 5 ]


print(quick_sort(0, len(arr) - 1, arr))
    
# This code is contributed by Adnan Aliakbar
