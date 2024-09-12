class Twitter:

    def __init__(self):
        self.tweets = []
        self.followers = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int):
        count = 0
        index = len(self.tweets) - 1
        feed = []
        if userId in self.followers:
            check = self.followers[userId]
        else:
            check = set([userId])
        while index >= 0 and count < 10:
            if  self.tweets[index][0] in check:
                feed.append(self.tweets[index][1])
                count += 1
            index -= 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:

            self.followers[followerId].add(followeeId)
        else:
            self.followers[followerId] = set([followerId, followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)