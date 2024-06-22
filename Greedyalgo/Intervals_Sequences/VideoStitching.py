import sys
from typing import List


def videoStitching(clips: List[List[int]], time: int) -> int:
    clips.sort()
    print(clips)
    dp = [sys.maxsize] * 101
    n = len(clips)
    dp[0] = 0 # for first 0 there is no time needed

    for s,e in clips:
        for i in range(s,e + 1):
            print(i,s,dp)
            dp[i] = min(dp[i],dp[s] + 1)

    return dp[time] if dp[time] < sys.maxsize else -1

if __name__ == '__main__':
    # print(videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10))
    print(videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9))