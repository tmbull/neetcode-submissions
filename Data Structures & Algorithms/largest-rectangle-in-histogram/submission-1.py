class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # iterate through the list
        # need to keep track of:
        # current max_area
        # current min_height
        # how to know when to move left bound?
        stack = [] # (idx, height)
        max_area = 0
        length = len(heights)
        for idx,height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                (idx_h,height_h) = stack.pop()
                max_area = max(max_area, (idx - idx_h) * height_h)
                start = idx_h

            stack.append((start, height))

        while stack:
            (idx_h,height_h) = stack.pop()
            max_area = max(max_area, (length - idx_h) * height_h)

        return max_area


            
        