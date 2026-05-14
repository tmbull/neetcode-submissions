class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # from any point
            # can go U/D/L/R if heights[dir] <= heights[curr]
            # brute force:
                # from 0,0 find all pacific cells
                # from -1,-1 find all atlantic cells
                # return intersection
        rows = len(heights)
        cols = len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prev_height):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r,c) in visit or
                prev_height > heights[r][c]):
                return
            
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacific, -1)
            dfs(rows - 1, c, atlantic, -1)

        for r in range(rows):
            dfs(r, 0, pacific, -1)
            dfs(r, cols - 1, atlantic, -1)

        results = [[r, c] for (r, c) in pacific.intersection(atlantic)]
        return results


        
        