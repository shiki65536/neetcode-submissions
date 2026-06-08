class Twitter:

    def __init__(self):
        self.t = 0
        self.tw = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.fw = defaultdict(set)  # userId -> set of followeeId        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tw[userId].append((self.t, tweetId))
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.fw[userId] | {userId}
        h = []
        for u in users:
            arr = self.tw[u]
            if arr:
                i = len(arr) - 1
                t, tid = arr[i]
                heapq.heappush(h, (-t, tid, u, i - 1))
        res = []
        while h and len(res) < 10:
            nt, tid, u, i = heapq.heappop(h)
            res.append(tid)
            if i >= 0:
                t, tid2 = self.tw[u][i]
                heapq.heappush(h, (-t, tid2, u, i - 1))
        return res       

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.fw[followerId].add(followeeId)    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fw[followerId].discard(followeeId)        
