# A O(n^2) time and O(n) extra
# space solution in Python3
def findLength(string, n):

    Sum = [0] * (n + 1)

    for i in range(1, n + 1):
        Sum[i] = (Sum[i - 1] +
            int(string[i - 1])) # convert chars to int
    print(Sum)
    ans = 0 # initialize result

    # consider all even length
    # substrings one by one
    for length in range(2, n + 1, 2):
    
        for i in range(0, n - length + 1):
        
            j = i + length - 1

            # Sum of first and second half
            # is same than update ans
            if (Sum[i + length // 2] -
                Sum[i] == Sum[i + length] -
                Sum[i + length // 2]):
                ans = max(ans, length)
    
    return ans

 # Driver code
if __name__ == "__main__":

     string = "123123"
    print("Length of the substring is",
        findLength(string, len(string)))
    
# This code is contributed
# by Rituraj Jain
