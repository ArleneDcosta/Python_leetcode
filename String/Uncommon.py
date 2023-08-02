def solve(A,B):
    count = {}
    A = A.split(" ")
    B = B.split(" ")
    res = []
    for ele in A:
        if ele in countA:
            count[ele] +=1
        else:
            count[ele] = 1

    for ele in B:
        if ele in countB:
            countB[ele] +=1
        else:
            countB[ele] = 1
                
    for ele in count:
        if count[ele]==1:
            res.append(ele)
    return res

print solve("this apple is sweet","this apple is sour")
    
