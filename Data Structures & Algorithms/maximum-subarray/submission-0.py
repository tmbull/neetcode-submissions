class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = float('-inf')
        max_sum = curr

        for num in nums:
            curr = max(curr, 0)
            curr += num

            max_sum = max(max_sum, curr)

        return max_sum