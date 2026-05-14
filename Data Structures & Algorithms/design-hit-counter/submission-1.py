class HitCounter:
    # need to track all timestamps
    # safe to assume that timestamps are recieved in order (meaning we can append to the end of a list)
    # to get hits in last timestamp, need to (a) find the timestamp and then iterate backwards from there
    # binary search O(log n)
        # is there a faster way? If getHits is also always the current timestamp then yes, we can just use a deque
        # That seems to be the case
    def __init__(self):
        self.hits = deque()
        

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        beginning = timestamp - 300
        while self.hits and self.hits[0] <= beginning:
            self.hits.popleft()

        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
