class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [0] * (2*len(nums))
        length = len(nums)
        for i in range(length):
            res[i] = nums[i]
            res[i + length] = nums[i]
            # i = 0
            # 2 * 0 = 0
            # 2 * 1 = 0 (i + 1)
            # 2 * 2 = 4 2(i + 1)
            # 2 * 3 = 6 2(i + 1) = 2*2 + 2 = 6
        return res