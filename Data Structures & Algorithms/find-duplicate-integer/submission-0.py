class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # easy soln O(n) space:
        # add all of the items to a set
        # return the result when it is found to already exist in the set
        # O(1) space... 
        # Two pointer solution
            # if we iterate at two different rates, we should eventually 
            # find the duplicate, similar to the cycle problem
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast:
                break

        head = 0
        while True:
            slow = nums[slow]
            head = nums[head]
            if slow == head:
                return slow


