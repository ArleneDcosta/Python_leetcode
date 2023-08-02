# Function to return max sum such that
# no two elements are adjacent
def find_max_sum(arr):
    incl = 0
    excl = 0
	
    for i in arr:
		
		# Current max excluding i (No ternary in
		# Python)
	new_excl = excl if excl>incl else incl
		
		# Current max including i
	incl = excl + i
	excl = new_excl
	
	# return max of incl and excl
    return (excl if excl>incl else incl)

# Driver program to test above function
arr = [1,2,9,4,5,0,4,11,6]
print find_max_sum(arr)

# This code is contributed by Kalai Selvan
