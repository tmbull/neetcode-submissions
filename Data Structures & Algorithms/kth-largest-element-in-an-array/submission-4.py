class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify then pop k
        # O(n + klogn)
        # heap = []
        # for n in nums:
        #     heapq.heappush(heap, -1 * n)
        # while k > 1:
        #     heapq.heappop(heap)
        #     k -= 1

        # return -1 * heap[0]

        # quick select
        # O(n + n/2 + n/4 ...) = O(2n) = O(n)
        length = len(nums)
        k = length - k
        left, right = 0, length - 1

        def quickSelect(l, r):
            p = l
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, length - 1)




