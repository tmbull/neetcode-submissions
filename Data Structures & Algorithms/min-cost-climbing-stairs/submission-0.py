def minCost(cost: List[int], current: int, i: int) -> int:
    n = len(cost)
    if i >= n:
        return current
    else:
        current += cost[i]
        return min(minCost(cost, current, i + 1), minCost(cost, current, i + 2))

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(minCost(cost, 0, 0), minCost(cost, 0, 1))
    