class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for s, d, w in times:
            adj[s].append((d, w))

        heap = []
        heapq.heappush(heap, (0, k))
        # track all visited nodes so that we can determine if all nodes get visited and what the max is
        visit = {}
        while heap:
            weight, dest = heapq.heappop(heap)
            if dest in visit:
                continue
            visit[dest] = weight
            
            neighbors = adj[dest]
            for neighbor, weight2 in adj[dest]:
                if neighbor not in visit:
                    heapq.heappush(heap, (weight + weight2, neighbor))

        if len(visit) != (n):
            return -1

        return max(visit.values())