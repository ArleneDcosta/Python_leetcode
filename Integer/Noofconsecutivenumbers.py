# Python program to count number of ways to 
# express N as sum of consecutive numbers. 
'''
The idea is to represent N as a sequence of length L+1 as:
N = a + (a+1) + (a+2) + .. + (a+L)
=> N = (L+1)*a + (L*(L+1))/2
=> a = (N- L*(L+1)/2)/(L+1)
We substitute the values of L starting from 1 till L*(L+1)/2 < N
If we get 'a' as a natural number then the solution should be counted.'''
def countConsecutive(N): 
	
	# constraint on values of L gives us the 
	# time Complexity as O(N^0.5) 
	count = 0
	L = 1
	while( L * (L + 1) < 2 * N): 
		a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1) 
		if (a - int(a) == 0.0): 
			count += 1
		L += 1
	return count 

# Driver code 

N = 15
print countConsecutive(N) 
N = 10
print countConsecutive(N) 

# This code is contributed by Sachin Bisht 
