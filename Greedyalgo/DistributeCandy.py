def candy(A):
    n = len(A)
    data = sorted((x,i) for i,x in enumerate(A))
    print(data)
    candies = [1] * n
    for _,i in data:
        if i > 0 and A[i] > A[i-1]:
            candies[i] = max(candies[i],candies[i-1] + 1)

        if i < n-1 and A[i] > A[i+1]:
            candies[i] = max(candies[i],candies[i+1] + 1)

    return sum(candies)

print(candy([1,2,7,4,3,3,1]))

print(candy([1,2,2]))
