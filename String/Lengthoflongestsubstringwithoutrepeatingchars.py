# Here, we are planning to implement a simple sliding window methodology

def longestUniqueSubsttr(string):
    
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0

    # starting the initial point of window to index 0
    start = 0
    
    for end in range(len(string)):

        # Checking if we have already seen the element or not
        if string[end] in seen:

            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)

        # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length

# Driver Code
string = "geeksforgeeks" 
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)
