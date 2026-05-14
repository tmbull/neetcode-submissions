class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate from top left to bottom right
        # if I encounter an unvisited island
            # increment island counter
            # map the entire island, marking it as visited
            # go back to main iteration
        
        r = 0
        c = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0

        def visit_island(r, c):
            if r < 0 or c < 0 or \
                r >= ROWS or c >= COLS or \
                (r,c) in visited or grid[r][c] == "0":
                    return
            visited.add((r,c))

            visit_island(r, c - 1)
            visit_island(r, c + 1)
            visit_island(r + 1, c)
            visit_island(r - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    visit_island(r,c)

        return islands

        