import math
def getPermutation(n, k):
    lists = list(range(1,n+1))
    result = ''
    n_copy = n
    print(n_copy)
    while n>0:
        #K is position and divisor is the no of permutions completed keeping 1 elem
        #constant(remaining digits)
        divisor = math.factorial(n - 1)
        print(f"Divisor {divisor}")
        #Quotient = Dividend/Divisor
        index = math.ceil(k/divisor) -1
        print(f"K is {k},Index is {index},List is {lists},{k/divisor}")
        pop = lists.pop(index)
        result = result + str(pop)
        n = n -1
        if k>divisor:
            #Remainder = Dividend – (Divisor x Quotient)
            k = (k - index*divisor)
    return result

print(getPermutation(3,3))
print(getPermutation(4,2))
print(getPermutation(3,1))
print(getPermutation(2,2))
print(getPermutation(3,6))
print(getPermutation(4,17))
