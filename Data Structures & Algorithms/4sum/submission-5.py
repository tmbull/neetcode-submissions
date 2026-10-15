class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        two pointer solution like 3 sum, but with an additional pointer at the beginning

        for i from 0 to len-3
            for j from i+1 to len-2
                l from 0 and r from len-1 down
        '''
        nums.sort()
        results = []
        for i in range(0, len(nums)-3):
            # if i and i-1 are the same, move forward to avoid dups
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                # for each unique i, if we find a duplicate j, we can continue as well
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                sub_target = target - (nums[i] + nums[j])
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    left_plus_right = nums[left] + nums[right]
                    if left_plus_right == sub_target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif left_plus_right < sub_target:
                        left += 1
                    else:
                        right -= 1
        
        return results