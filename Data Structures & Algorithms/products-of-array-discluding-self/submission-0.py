class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # naive solution
        # iterate through nums once for each index O(n**2)
        # better calculate product and then divide for each element
        # results[i] = results[i-1] * results[i+1]
            # calculate the reuslt in each direction and then find result
        forward = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            forward[i] = product

        product = 1
        rev = [0] * len(nums)
        for i in reversed(range(len(nums))):
            product *= nums[i]
            rev[i] = product

        result = [0] * len(nums)
        result[0] = rev[1]
        result[-1] = forward[-2]

        for i in range(1, len(nums) - 1):
            result[i] = forward[i - 1] * rev[i + 1]

        return result