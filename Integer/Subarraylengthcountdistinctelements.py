def sumoflength(arr, n):
# For maintaining distinct elements.
    s = []

    # Initialize ending point and result
    j = 0
    ans = 0

    # Fix starting point
    for i in range(n):
        
        # Find ending point for current
        # subarray with distinct elements.
        while (j < n and (arr[j] not in s)):
            print arr[j],s,j
            s.append(arr[j])
            j += 1

        # Calculating and adding all possible
        # length subarrays in arr[i..j]
        ans += ((j - i) * (j - i + 1)) // 2
        print ans 
        # Remove arr[i] as we pick new
        # stating point from next
        s.remove(arr[i])

    return ans

# Driven Code
if __name__=="__main__":
    
    arr = [1, 2, 3, 4]
    n = len(arr)
    print(sumoflength(arr, n))

# This code is contributed by ita_c
