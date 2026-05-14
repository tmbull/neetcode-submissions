class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        # iterate through nums, calculate one = target - nums[i]
        # if we've seen "one", return one, two
        for i in range(len(nums)):
            second = nums[i]
            first = target - nums[i]
            if first in seen:
                return [seen[first], i]
            else:
                seen[second] = i
        
        return []