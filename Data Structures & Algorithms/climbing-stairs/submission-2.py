class Solution:
    def climbStairs(self, n: int) -> int:
        # go step by step, recursively trying each combination of
        # memo = [None] * n
        # return self.climbSteps(memo, 0, n)
        one, two = 1, 1

        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp

        return one
        
    # def climbSteps(self, memo, i: int, n: int) -> int:
    #     if i == n:
    #         return 1
    #     elif i > n:
    #         return 0
    #     elif not memo[i]:
    #         memo[i] = self.climbSteps(memo, i + 1, n) + self.climbSteps(memo, i + 2, n)

    #     return memo[i]