class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # put all intervals on a number line
        # for each query, iterate through intervals until we find
        intervals.sort()
        heap = []
        iq = 0
        ii = 0
        results = {}
        for q in sorted(queries):
            while ii < len(intervals) and intervals[ii][0] <= q:
                start, end = intervals[ii]
                heapq.heappush(heap,  (end - start + 1, end))
                ii += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            results[q] = heap[0][0] if heap else -1

        return [results[q] for q in queries]

        