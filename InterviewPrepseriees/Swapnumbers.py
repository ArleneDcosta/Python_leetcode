from heapq import heapify,heappop,heappush

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)  # Convert num to string for easy manipulation
        n = len(num_str)
        max_num = num  # Track the maximum number found

        # Try all possible swaps
        for i in range(n):
            for j in range(i + 1, n):
                num_list = list(
                    num_str
                )  # Convert the string to list for swapping

                num_list[i], num_list[j] = (
                    num_list[j],
                    num_list[i],
                )  # Swap digits at index i and j
                temp = int(
                    "".join(num_list)
                )  # Convert the list back to string and then to integer

                max_num = max(
                    max_num, temp
                )  # Update max_num if the new number is larger

        return max_num  
    
def maximumSwap(num: int) -> int:
    num_str = list(str(num))
    n = len(num_str)
    max_right_index = [0] * n
    print(max_right_index)

    max_right_index[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        max_right_index[i] = (
            i
            if num_str[i] > num_str[max_right_index[i + 1]]
            else max_right_index[i + 1]
        )
    print(max_right_index)
    for i in range(n):
        if num_str[i] < num_str[max_right_index[i]]:
            num_str[i], num_str[max_right_index[i]] = (
                num_str[max_right_index[i]],
                num_str[i],
            )
            return int("".join(num_str))

    return num

def match(curr, res):
  
    if curr > res:
        res = curr
    return res

# Function to set highest possible digits
# at given index
def setDigit(s, index, res, k):
  
    # Base case: If no swaps left or index reaches 
    # the last character, update result
    if k == 0 or index == len(s) - 1:
        res = match(s, res)
        return res

    maxDigit = 0

    # Finding maximum digit for placing at given index
    for i in range(index, len(s)):
        maxDigit = max(maxDigit, int(s[i]))

    # If the digit at current index is already max
    if int(s[index]) == maxDigit:
        res = setDigit(s, index + 1, res, k)
        return res

    # Try swapping with the maximum digit found
    for i in range(index + 1, len(s)):
      
        # If max digit is found at current position
        if int(s[i]) == maxDigit:
          
            # Swap to get the max digit at the required index
            s = swap(s, index, i)

            # Call the recursive function to set the next digit
            res = setDigit(s, index + 1, res, k - 1)

            # Backtrack: swap the digits back
            s = swap(s, index, i)

    return res

# Function to swap characters in the string
def swap(s, i, j):
  
    # Convert string to list for mutation,
    # then back to string
    s_list = list(s)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)

# Function to find the largest number after k swaps
def findMaximumNum(s, k):
    res = s
    res = setDigit(s, 0, res, k)

    # Returning the result
    return res

# using Recursion

def findMax(s, k):
  
    # Base case: If no swaps are allowed
    if k == 0:
        return s

    n = len(s)
    ans = s

    # Iterate through all character pairs
    for i in range(n - 1):
        for j in range(i + 1, n):

            # Swap only if s[j] > s[i]
            if s[i] < s[j]:
                
                # Perform the swap
                swapped = list(s)
                swapped[i], swapped[j] = swapped[j], swapped[i]
                swapped = ''.join(swapped)

                # Recur to check maximum with
                # one less swap allowed
                rec_result = findMax(swapped, k - 1)
                if rec_result > ans:
                    ans = rec_result

    return ans

def findMaximumNum(s, k):
  
    # Wrapper function to find result
    return findMax(s, k)

if __name__ == '__main__':
    print(maximumSwap(num = 2736))
    print(maximumSwap(num = 9973))
    print(maximumSwap(num = 1993))
    print(maximumSwap(num = 12))