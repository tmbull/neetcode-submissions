class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = set(nums)

        longest = 0
        for num in unique_nums:
            if (num - 1 not in unique_nums):
                result = 1
                while (num + result in unique_nums):
                    result += 1
                longest = max(longest, result)

        return longest
