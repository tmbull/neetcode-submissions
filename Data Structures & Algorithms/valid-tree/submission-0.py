class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        visited = set()
        def dfs(prev, curr) -> bool:
            if curr in visited:
                return False
            
            visited.add(curr)
            for i in adj[curr]:
                if i == prev:
                    continue
                if not dfs(curr, i):
                    return False

            return True

        return dfs(-1, 0) and len(visited) == n