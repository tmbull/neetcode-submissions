class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max heap - negate values before pushing them
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(f"{x} --- {y}")

            if x != y:
                heapq.heappush(stones, x - y)

        if stones:
            return -1 * stones[0]
        else:
            return 0
