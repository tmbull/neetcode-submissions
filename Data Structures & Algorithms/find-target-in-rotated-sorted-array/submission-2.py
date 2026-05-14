class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # two parts:
            # find point of rotation
            # search for target within the appropriate side
        start_idx = find_start(nums)
        if target == nums[start_idx]:
            return start_idx
        elif target > nums[start_idx] and target <= nums[-1]:
            return find_target(nums, start_idx, len(nums), target)
        else:
            return find_target(nums, 0, start_idx, target)
        

def find_start(nums: List[int]) -> int:
    left = 0
    right = len(nums)
    idx = 0

    while left < right:
        idx = (left + right) // 2
        if nums[idx] < nums[idx - 1]:
            return idx
        elif nums[idx] < nums[0]:
            right = idx
        else:
            left = idx + 1

    return idx

def find_target(nums: List[int], left, right, target) -> int:
    while left < right:
        idx = (left + right) // 2
        if nums[idx] == target:
            return idx
        elif nums[idx] < target:
            left = idx + 1
        else:
            right = idx
    
    return -1