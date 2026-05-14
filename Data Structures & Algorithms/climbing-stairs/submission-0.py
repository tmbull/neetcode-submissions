class Solution:
    def climbStairs(self, n: int) -> int:
        # go step by step, recursively trying each combination of
        return self.climbSteps(0, n)
        
    def climbSteps(self, i: int, n: int) -> int:
        if i == n:
            return 1
        elif i > n:
            return 0
        else:
            return self.climbSteps(i + 1, n) + self.climbSteps(i + 2, n)