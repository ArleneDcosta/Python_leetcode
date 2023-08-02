def seats(A):
    MOD = 10000003
    # all the indices of xs
    crosses = [i for i,c in enumerate(A) if c == "x"]
    print(crosses)
    # moves req assuming starting position is 0
    crosses = [(cross - i) for i,cross in enumerate(crosses)]
    print(crosses)
    n = len(crosses)
    if n == 0: return 0

    ans = float('inf')
    #Time complexity is too much. Hence avoid this method
    #Find the median of the array
    segment_start = crosses[n // 2]
    print(n)
    #for segment_start in range(len(A)):
    print(segment_start)
    total = 0
    #no of moves
    for cross in crosses:
        total += abs(cross - segment_start)
        total %= MOD
    ans = min(ans, total % MOD)
    return ans
if __name__ == '__main__':
    print(seats("..x..x...xx.."))
