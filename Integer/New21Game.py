def new21Game(N, K, W):
    dp = [0.0] * (N + W + 1)
    # dp[x] = the answer when Alice has x points
    for k in xrange(K, N + 1):
        dp[k] = 1.0
    print dp
    S = min(N - K + 1, W)
    #eg 21-17 is lesser than 10 meaning if 17 then prob will only be 5
    # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
    for k in xrange(K - 1, -1, -1):
        dp[k] = S / float(W)
        print k,dp[k],dp[k + W]
        S += dp[k] - dp[k + W]
        print k,k+W,S
    print dp
    return dp[0]


#print new21Game(10,1,10)
#print new21Game(6,1,10)
print new21Game(10,2,10)
#print new21Game(21,17,10)
'''Alice starts with 0 points, and draws numbers while she has less than K
points.  During each draw, she gains an integer number of points randomly
from the range [1, W], where W is an integer.
Each draw is independent and the outcomes have equal probabilities.'''
#max score from n+w+1
#to win value has to be between n and w.if greater she loses
# on 21 if she gets 10 she gets 31 so n+w+1 is max
#here nor less than n probability has to be reached from k times
#initial points is0 but imagine she is at 16 point she can
#get any point between 1 and 10 so value will be 26
#k when we aldready have k points
''' be the answer when we already have x points. When she has between K and N
points,
then she stops drawing and wins. If she has more than N points, then she loses.
'''
''''
1.)Alice draws numbers when she has less than k points
2.)She should have values between k and n to win if greater than n she loses.

'''
