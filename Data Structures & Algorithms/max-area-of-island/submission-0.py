class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        max_area = 0

        def visit_island(r,c) -> int:
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                (r,c) in visited or grid[r][c] == 0):
                return 0
            area = 1
            visited.add((r,c))

            area += visit_island(r, c - 1)
            area += visit_island(r, c + 1)
            area += visit_island(r - 1, c)
            area += visit_island(r + 1, c)

            print(area)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, visit_island(r,c))

        return max_area

                