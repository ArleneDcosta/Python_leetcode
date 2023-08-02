def minDistance(word1, word2):
    #https://www.youtube.com/watch?v=XYi2-LPrwm4
    #Bottomup programming model
    #insert = (i,j+1)
    #delete = (i+1,j)
    #replace = (i+1,j+1)
    #w2 on j(horizontal)
    #w1 on i(vertical)
    cache  = [[float("inf")]* (len(word2)+1) ]* (len(word1)+1)
    print(cache)
    #Initializing last row based on word 2(see image)
    for j in range(len(word2)+1):
        cache[len(word1)][j] =  len(word2) - j

    #Initializing last col based on word 1(see image)
    for i in range(len(word1)+1):
        cache[i][len(word2)] =  len(word1) - i
    print(cache)
    for i in range(len(word1) -1,-1,-1):
        for j in range(len(word2) -1,-1,-1):
            if word1[i] == word2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                cache[i][j] = min(cache[i][j+1],cache[i+1][j],cache[i+1][j+1]) + 1
    return cache[0][0]



print(minDistance(word1 = "horse", word2 = "ros"))
#print(minDistance(word1 = "intention", word2 = "execution"))

