def isPowerOfFour(n):
    count = 0
    if (n and (not(n & (n - 1)))):
	while(n > 1):
	    n >>= 1
	    count += 1
		
	if(count % 2 == 0):
	    return True
	else:
	    return False

# Driver code
test_no = 64
if(isPowerOfFour(64)):
	print(test_no, 'is a power of 4')
else:
	print(test_no, 'is not a power of 4')


 
