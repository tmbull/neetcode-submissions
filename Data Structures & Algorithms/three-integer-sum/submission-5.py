class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        two sum - 2 pointer algorithm
        set left and right
        if sum == target, add to result and break
        if sum > target, decrement right
        else, increment left
        O(nlogn) for sort, O(n^2) for collecting results
        better than O(n^3) for brute force
        '''
        nums.sort()
        results = []
        for fixed in range(0, len(nums)-2):
            # We need at least one non-positive number to get a sum equal to 0
            if nums[fixed] > 0:
                break
            # skip duplicate fixed numbers
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue
            target = 0 - nums[fixed]
            left = fixed + 1
            right = len(nums) - 1
            while left < right:
                result = nums[left] + nums[right]
                if  result == target:
                    results.append([nums[fixed], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif result < target:
                    left += 1
                else:
                    right -= 1
        
        return results
