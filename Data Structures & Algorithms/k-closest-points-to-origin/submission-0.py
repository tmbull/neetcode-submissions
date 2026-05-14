class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We can either add all of the elements to a list and then sort by distance or add them to a heap and pop off the first k elements
        point_distance = [[self.distance(pair), pair[0], pair[1]] for pair in points]
        heapq.heapify(point_distance)
        print(point_distance)
        results = []
        for i in range(k):
            results.append(heapq.heappop(point_distance)[1:3])

        return results

    def distance(self, pair: List[int]) -> int:
        return math.sqrt(pair[0]**2 + pair[1]**2)