class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = defaultdict(int)
        for num in nums[:k]:
            window[num] += 1
        results.append(max(window))

        for i in range(k, len(nums)):
            print(f"{i} {k}")
            window[nums[i]] += 1
            window[nums[i-k]] -= 1
            if window[nums[i-k]] == 0:
                del(window[nums[i-k]])
            results.append(max(window))


        return results