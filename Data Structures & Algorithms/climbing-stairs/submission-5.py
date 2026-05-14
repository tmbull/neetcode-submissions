class Solution:
    def climbStairs(self, n: int) -> int:
        # bottom up DP
        # base cases
            # 1 stairs: 1 way
            # 2 stairs: 2 way
        # other cases:
            # dp[n] = dp[n - 1] + dp[n - 2]
            # 3 stairs:
            # 0 -> 1 -> 3
            # 0 -> 2 -> 3
            # 0 -> 1 -> 2 -> 3
        dp = [1, 2]
        if n < 2:
            return dp[n-1]

        for i in range(3, n+1):
            result = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = result

        return dp[1]