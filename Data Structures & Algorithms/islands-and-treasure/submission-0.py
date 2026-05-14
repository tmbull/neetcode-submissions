class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        water = -1
        treasure = 0
        land = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                
        # approach: traverse entire grid
        # when encountering a water cell, skip
        # when encountering a land cell, skip
        # when encountering a treasure cell, do BFS outward from the cell marking all land cells of min(curr, distance)
        def bfs(origin_r, origin_c): 
            q = deque()
            visit = set()
            q.append((origin_r, origin_c))

            curr = 0
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    if (r < 0 or c < 0 or r >= rows or c >= cols or 
                        grid[r][c] == water or
                        (r, c) in visit):
                        continue

                    visit.add((r, c))
                    grid[r][c] = min(grid[r][c], curr)
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        q.append((new_r, new_c))

                curr += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == treasure:
                    print(f"treasure at (r, c)")
                    bfs(r,c)