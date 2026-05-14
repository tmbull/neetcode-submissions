class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)
        start = 0
        while start < end:
            idx = start + ((end - start) // 2)
            print(f"{nums[idx]}: {idx}")
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                end = idx
            else:
                start = idx + 1
        
        return -1
