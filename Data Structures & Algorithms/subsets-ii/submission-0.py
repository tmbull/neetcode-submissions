class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        curr_set = []
        # very important that nums are sorted so iterating past dups works
        nums.sort()
        
        def helper(i, results, curr_set):
            if i >= len(nums):
                results.append(curr_set.copy())
                return
            
            # decision to include nums[i]
            curr_set.append(nums[i])
            helper(i + 1, results, curr_set)

            #decision to not include nums[i] (or dups)
            curr_set.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i + 1, results, curr_set)

        helper(0, results, curr_set)

        return results