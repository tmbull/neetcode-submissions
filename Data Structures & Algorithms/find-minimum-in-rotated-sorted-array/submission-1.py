class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min is nums[i] where nums[i] < nums[i - 1]
        # O(n) iterate until the above is true
        # O(log n) binary search
            # nums[i] > nums[i]:
            # if nums[i] > nums[0]:
                # move left to i
            # else
                # move right to i
        left = 0
        right = len(nums)
        while left < right:
            idx = (left + right) // 2
            if nums[idx] < nums[idx - 1]:
                return nums[idx]
            elif nums[idx] > nums[0]:
                left = idx + 1
            else:
                right = idx

        return nums[0]