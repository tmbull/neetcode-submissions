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

        self.tweets = defaultdict(list)
        self.curr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.curr, tweetId))
        self.curr -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        results = []
        heap = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(heap, (count, tweetId, followee, index - 1))

        while heap and len(results) < 10:
            count, tweetId, followee, index = heapq.heappop(heap)
            results.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(heap, (count,  tweetId, followee, index - 1))

        return results
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
