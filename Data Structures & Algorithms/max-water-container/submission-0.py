class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        result = 0

        while l < r:
            result = max(result, min(heights[l],heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return result
