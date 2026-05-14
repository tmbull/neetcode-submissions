class Logger:
    # need to save unique messages over the last 10 seconds
    # options: dict msg -> timestamp?
        # need to prune in bground periodically 
        # set - won't work, we need timestamp to validate

    def __init__(self):
        self.msgs = {}

        

    # cases:
    # 1. message not in cache - add message, return true
    # 2. message in cache and expired, update timestamp and return true
    # 3. message in cache and not expired, don't update timestamp and return false
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.msgs:
            if timestamp - self.msgs[message] < 10:
                return False

        self.msgs[message] = timestamp
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
