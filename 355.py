class Twitter:

    def __init__(self):
        self.count = 0 #used as an identifier for our heap
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # post a pair [count, tweetId]
        # reminder to self: don't use minHeap of size 10 here, still want to store all tweets...
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # decrement bc of Python min heap

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # make sure the user follows themself to not miss their own tweets
        self.followMap[userId].add(userId)

        # iterate through the list of following and fetch their latest tweet, and add to a heap
        for user in self.followMap[userId]:
            # make sure this user has tweets
            if self.tweetMap[user]:
                # fetch the last tweet
                lastIndex = len(self.tweetMap[user]) - 1
                count, lastTweetId = self.tweetMap[user][lastIndex]
                heapq.heappush(minHeap, [count, lastTweetId, user, lastIndex-1])
        
        # pop everything from the heap, and if we still need more tweetes, iterate again
        while minHeap and len(res) < 10:
            count, lastTweetId, user, lastIndex = heapq.heappop(minHeap)
            res.append(lastTweetId)
            
            # appending this user's previous tweet (2nd last)
            if lastIndex >= 0:
                count, lastTweetId = self.tweetMap[user][lastIndex]
                heapq.heappush(minHeap, [count, lastTweetId, user, lastIndex-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # follower follows followee
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # make sure that the follow list is populated first
        if self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)