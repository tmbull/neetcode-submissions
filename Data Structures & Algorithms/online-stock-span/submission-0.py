class StockSpanner:
    # Naive soln:
        # Store the price for all time
        # Append price to the end, and iterate backwards to find the span
    # Do we need to store all prices?
        # What happens when we find a previous value > current value?
        # We no longer care about those values? not true
            # ex. [7,2,1,2] - 2 - span in 4
            #               - 8 - span in 5
            # So we have to save all values
        # How to short circuit span counting, what if we also save the span
        # [7, 2, 1, 2]
        # [1, 1, 1, 3], 4 -> [7] -> nope 3 + 1 = 4
        #             , 8 -> 3 + 1 + 1 = 5 still O(n) worst case?
        # monotonic stack
        # (7, 1), ()

    def __init__(self):
        self.stack = deque()
        

    def next(self, price: int) -> int:
        result = 1
        while self.stack:
            prev_price, prev_span = self.stack[-1]
            if prev_price <= price:
                self.stack.pop()
                result += prev_span
            else:
                break
        self.stack.append((price,result))
        return result
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)