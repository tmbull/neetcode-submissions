class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # need to track how many times each number is in the array
        # dict num -> count
        # iterate dict to find k most
        # 2 n time and 3n space
        # is there a more efficient way? yes, bucket sort
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] = counts[n] + 1
            else:
                counts[n] = 1
        
        heap = []
        for val, count in counts.items():
            heapq.heappush(heap, (-count, val))
        
        result = []
        count = 0
        for _ in range(k):
            (_, val) = heapq.heappop(heap)
            result.append(val)

        return result