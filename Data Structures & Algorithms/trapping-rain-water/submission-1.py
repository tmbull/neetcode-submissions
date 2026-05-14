class Solution:
    def trap(self, height: List[int]) -> int:
        # need to map all of the "valleys" in the map
        # go from left to right, if peak, mark the peak as L and iterate to next peak >= L and mark it as R
        # Iterate from L to R, if less than last peak, add min(L, R) - curr
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] * len(height)
        water = 0

        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i])

        for i in reversed(range(0, len(height)-1)):
            max_right[i] = max(max_right[i+1], height[i])

        for i in range(1, len(height) - 1):
            water += min(max_left[i], max_right[i]) - height[i]

        
        return water