def numDupDigitsAtMostN(N):
    T = [9,261,4725,67509,831429,9287109,97654149,994388229]
    # here remaining values are eliminated from total
    t = [99,999,9999,99999,999999,9999999,99999999,999999999]
    #here precalcuated values above[100 has 10 and 99 has 9]
    if N < 10:
    	return 0
    L = len(str(N))
    m, n = [1], []
    #11 is max llenght of no possible
    g = 11-L
    print g
    #n has set of individual digits and m has
    for i in range(L):
    	n.append(int(str(N)[i]))
    	print 'n',n
    	m.append(g)
    	print 'm',m
    	#1 more than 11 0 is 1 so implicity 1 added
    	g = g*(12-L+i)#probability 
    	print 'g',g
    S = 0
    for i in range(L):
        print 'check',len(set(n[:L-i-1])),len(n)-i-1
        if len(set(n[:L-i-1])) != len(n)-i-1:
            continue
        k = 0
        #removal of unnecessary numbers which do not have repeating
        # the no and the highest number in t
        for j in range(10):
             if j not in n[:L-i-1] and j > n[L-i-1]:
                k += 1
                print n[L-i-1],k,j,n[:L-i-1]
        S += k*m[i]
        print S
        #S is the total no of non numbers in reson list
    print T[L-2],N,S
    return(T[L-2]-(t[L-2]-N-S))

print numDupDigitsAtMostN(10)
#80 abive 11 not following till 99
#11 include 91[includes above no not fol and both]
# 8 is above 11 following till 99
# 9 - [99 - 80-11] total - com no foll - req
# thus 8 becomes the following above 11 till 99

