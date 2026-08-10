class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        followees = self.followMap.get(userId, set())

        target_users = list(followees)
        target_users.append(userId)

        for followeeId in target_users:
            if followeeId in self.tweetMap and len(self.tweetMap) > 0:
                idx = len(self.tweetMap[followeeId]) - 1
                cnt, tweet_id = self.tweetMap[followeeId][idx]

                minHeap.append((cnt, tweet_id, followeeId, idx - 1))  
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweet_id, followeeId, index = heapq.heappop(minHeap)
            res.append(tweet_id)

            if index >= 0:
                count, tweet_id = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, (count, tweet_id, followeeId, index - 1))
        return res      

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)
