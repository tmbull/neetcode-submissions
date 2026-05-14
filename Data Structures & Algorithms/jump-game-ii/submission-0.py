class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0

        while r < len(nums) - 1:
            curr_max = 0
            for i in range(l, r + 1):
                curr_max = max(curr_max, i + nums[i])
            l = r + 1
            r = curr_max
            res += 1
        return res