class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # similar to subsets except we can use any number
        # multiple times and we also care about the sum
        # 
        
        result = []

        def dfs(i, combo, total):
            if total == target:
                result.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return

            combo.append(nums[i])
            dfs(i, combo, nums[i] + total)
            combo.pop()
            dfs(i + 1, combo, total)

        dfs(0, [], 0)

        return result
        