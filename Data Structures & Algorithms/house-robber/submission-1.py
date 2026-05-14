class Solution:
    def rob(self, nums: List[int]) -> int:
        # for each house, we can either rob:
        # house[n] + max(house[n-2] or
        # max(house[n-1]

        dp = [0]*2

        for num in nums:
            result = max(dp[0] + num, dp[1])
            dp[0] = dp[1]
            dp[1] = result

        return dp[1]
        