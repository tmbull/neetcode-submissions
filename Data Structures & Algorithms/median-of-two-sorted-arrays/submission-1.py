class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # median of one array: find the middle element
        # special cases:
            # no overlap - order the arrays and find the (m + n) / 2 index
            # overlap - need to find the place where idx_1 + idx_2 = (m + n) / 2
            # even # of elements, need to find two index and average their values

        length = len(nums1) + len(nums2)
        is_even = length % 2 == 0
        part = length // 2

        small, big = nums1, nums2
        if len(small) > len(big):
            small, big = big, small
        l1 = 0
        r1 = len(small) - 1

        while True:
            idx1 = (l1 + r1) // 2
            idx2 = part - idx1 - 2

            small_l = small[idx1] if idx1 >= 0 else float('-inf')
            small_r = small[idx1+1] if (idx1 + 1) < len(small) else float('inf')
            big_l = big[idx2] if idx2 >= 0 else float('-inf')
            big_r = big[idx2 + 1] if (idx2 + 1) < len(big) else float('inf')
            if small_l > big_r:
                r1 = idx1  - 1
            elif big_l > small_r:
                l1 = idx1 + 1
            else:
                if is_even:
                    return (max(small_l, big_l) + min(small_r, big_r)) / 2
                else:
                    return min(small_r, big_r)
            
            
