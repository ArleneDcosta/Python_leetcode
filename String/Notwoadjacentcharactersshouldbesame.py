# Python3 implementation of the approach 

# Function that returns true if it is possible 
# to rearrange the characters of the String 
# such that no two consecutive characters are same 
def isPossible(Str): 

	# To store the frequency of 
	# each of the character 
	freq = dict() 

	# To store the maximum frequency so far 
	max_freq = 0
	for j in range(len(Str)): 
		freq[Str[j]] = freq.get(Str[j], 0) + 1
		if (freq[Str[j]] > max_freq): 
			max_freq = freq[Str[j]] 

	# If possible 
	if (max_freq <= (len(Str) - max_freq + 1)): 
		return True
	return False

# Driver code 
Str = "geeksforgeeks"

if (isPossible(Str)): 
	print("Yes") 
else: 
	print("No") 

# This code is contributed by Mohit Kumar 
