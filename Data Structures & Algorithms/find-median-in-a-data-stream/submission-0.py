class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)

        if len(self.small) + 1 < len(self.large):
            heapq.heappush(self.small, heapq.heappop(self.large) * -1)

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return self.small[0] * -1
        else:
            return ((self.small[0] * -1) + self.large[0]) / 2
        