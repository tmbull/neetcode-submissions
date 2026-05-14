class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # can count all of the items in a dict and then sort the 
        # items by value (count)
        # n + nlogn
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        buckets = [[] for i in range(len(nums) + 1)]

        for num, count in counts.items():
            buckets[count].append(num)

        results = []
        done = False
        for bucket in reversed(buckets):
            for num in bucket:
                results.append(num)
                if len(results) == k:
                    return results

        return results