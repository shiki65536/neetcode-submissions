class MedianFinder:

    def __init__(self):
        self.small = []
        self.large =[]


    def addNum(self, num: int) -> None:
        # 1) push into small first
        heapq.heappush(self.small, -num)

        # 2) ensure order: max(small) <= min(large)
        if self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # 3) rebalance sizes: small can have at most 1 extra
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)    

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0