class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i,num in enumerate(nums):
            # nums + x = target # target - nums = x
            x = target - num
            if x in found:
                return [found[x], i]
            else:
                found[num] = i

        raise Exception("Failed to find result")