# Python code to print largest permutation after K swaps

def KswapPermutation(arr, n, k):

    # Auxiliary array of storing the position of elements
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
        print pos
    for i in range(n):

        # If K is exhausted then break the loop
        if k == 0:
            break

        # If element is already largest then no need to swap
        if (arr[i] == n-i):
            continue

        # Find position of i'th largest value, n-i
        temp = pos[n-i]

        # Swap the elements position
        pos[arr[i]] = pos[n-i]
        pos[n-i] = i

         # Swap the ith largest value with the value at
        # ith place
        arr[temp], arr[i] = arr[i], arr[temp]

        # Decrement K after swap
        k = k-1

# Driver code
arr = [4, 5, 2, 1, 3]
n = len(arr)
k = 3
KswapPermutation(arr, n, k)

# Print the answer
print "Largest permutation after", k, "swaps: "
print " ".join(map(str, arr))
