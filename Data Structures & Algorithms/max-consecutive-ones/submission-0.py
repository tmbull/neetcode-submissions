class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        curr = 0
        for n in nums:
            if n == 1:
                curr += 1
            else:
                result = max(curr, result)
                curr = 0

        return max(result, curr)

        