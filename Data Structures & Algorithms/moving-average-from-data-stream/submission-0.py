class MovingAverage:
    # how to calculate moving average? 
    # sum previous n values
    # option 1:
    # save previous n values in a queue, pop first off the queue, then push current onto it, calculate sum
    # cons: sum calculation is sum of n values
    # how to "update" the average?

    # 1,2,3,4 n = 3
    # .,.,2,3 .. what if we save the total and update it instead of the average?
    # 1+2+3 = 6, / 3 = 2
    # 6 - 1 + 4 = 9, / 3 = 3
    # how to initialize? 

    def __init__(self, size: int):
        self.total = 0
        self.cache = deque([])
        self.size = size
        

    def next(self, val: int) -> float:
        if len(self.cache) == self.size:
            self.cache.append(val)
            self.total = self.total - self.cache.popleft() + val
        else:
            self.cache.append(val)
            self.total = self.total + val

        return self.total / len(self.cache)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
