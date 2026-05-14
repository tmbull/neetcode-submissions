class Twitter:
    # need to:
        # retrieve tweets by most recent to least recent
            # options:
                # stack 
                # maxHeap with increasing id
                # create a per-user feed and post the same tweet to all users feeds
                    # won't work well for unfollow
                    # tweets will have to be removed from feeds on unfollow
        # follow/unfollow
            # map of userId -> [userIds]
        # basic idea:
            # post tweets to a heap
    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = []
        self.curr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.curr, userId, tweetId))
        self.curr -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        count = 0
        for (i, u, t) in reversed(self.tweets):
            if count == 10:
                break
            if u == userId or u in self.follows[userId]:
                results.append(t)
                count += 1

        return results
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
