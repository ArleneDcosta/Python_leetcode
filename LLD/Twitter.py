from typing import List
import itertools
import collections
import heapq

class Twitter:

    def __init__(self):
        self.tweetsuser = {}
        self.followinglist = {}
        self.tweetstack = {}
        self.orderposts = []

    def addTweetsToStack(self,followerid,followeeid):
        if followerid not in self.tweetstack:
            self.tweetstack[followerid] = []
        if followeeid in self.tweetsuser and len(self.tweetsuser[followeeid]) != 0:
            self.tweetstack[followerid] += self.tweetsuser[followeeid]

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.followinglist:
            self.followinglist[userId] = [userId]

        if userId not in self.tweetsuser:
            self.tweetsuser[userId] = [tweetId]
        else:
            self.tweetsuser[userId].append(tweetId)

        if userId not in self.tweetstack:
            self.tweetstack[userId] = []
        
        for followers in self.followinglist[userId]:
            self.tweetstack[followers].append(tweetId)
        self.orderposts.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        if userId in self.tweetstack:
            for ele in self.orderposts:
                if ele in self.tweetstack[userId][::-1]:
                    result.append(ele)
            return result[::-1][0:10]
        else:
            return []

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followinglist:
            self.followinglist[followeeId] = [followeeId]
        if followerId not in self.followinglist[followeeId]:
            self.followinglist[followeeId].append(followerId)

            self.addTweetsToStack(followerId,followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print('Self.tweetstack',self.tweetstack)
        # print('Self.following list',self.followinglist)
        # print('Self.tweetuser',self.tweetsuser)
        for tweet in self.tweetsuser[followeeId]:
            if followerId in self.tweetstack and tweet in self.tweetstack[followerId] :
                self.tweetstack[followerId].remove(tweet)

        if followeeId in self.followinglist:
            if followerId in self.followinglist[followeeId]:
                self.followinglist[followeeId].remove(followerId)

class Twitteroptimized: 
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)

if __name__ == '__main__':
    twitter= Twitter()
    twitter.postTweet(1, 5) # User 1 posts a new tweet (id = 5).
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2)    # User 1 follows user 2.
    twitter.postTweet(2, 6) # User 2 posts a new tweet (id = 6).
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2)  # User 1 unfollows user 2.
    print(twitter.getNewsFeed(1))  # User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
    print("---------------------")

    twitter= Twitter()
    twitter.postTweet(1, 1) 
    print(twitter.getNewsFeed(1))  
    twitter.follow(2, 1)   
    print(twitter.getNewsFeed(2)) 
    twitter.unfollow(2,1) 
    print(twitter.getNewsFeed(2)) 
    print("---------------------")

    twitter= Twitter()
    twitter.postTweet(2, 5) 
    twitter.follow(1, 2)   
    twitter.follow(1, 2) 
    print(twitter.getNewsFeed(1)) 
    print("---------------------")

    twitter= Twitter()
    twitter.postTweet(1, 5) 
    twitter.follow(1, 2)   
    twitter.follow(2, 1) 
    print(twitter.getNewsFeed(2)) 
    twitter.postTweet(2, 6) 
    print(twitter.getNewsFeed(1)) 
    print(twitter.getNewsFeed(2))
    twitter.unfollow(2,1) 
    print(twitter.getNewsFeed(1)) 
    print(twitter.getNewsFeed(2))
    twitter.unfollow(1,2) 
    print(twitter.getNewsFeed(1)) 
    print(twitter.getNewsFeed(2))

    print("--------------------------")
    twitter= Twitter()
    twitter.postTweet(2, 5) 
    twitter.postTweet(1, 3) 
    twitter.postTweet(1, 101) 
    twitter.postTweet(2, 13) 
    twitter.postTweet(2, 10) 
    twitter.postTweet(1, 2) 
    twitter.postTweet(2, 94) 
    twitter.postTweet(2, 505) 
    twitter.postTweet(1, 333) 
    twitter.postTweet(1, 22) 
    print(twitter.getNewsFeed(2)) 
    twitter.follow(2, 1)   
    print(twitter.getNewsFeed(2)) 




