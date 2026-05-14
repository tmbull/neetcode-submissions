class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            minimum = min(self.min_stack[-1], val)
        else:
            minimum = val
        self.min_stack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.min_stack:
            return None
        else:
            return self.min_stack[-1]
        
