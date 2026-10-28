class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        maybe we can swap elements?

        keep track of elements that have been chosen
        

        dfs
            if all elements have been chosen
                add to results and return

            pick an element
            dfs
            pop element
        '''

        used = set()
        results = []

        def dfs(current):
            if len(current) == len(nums):
                results.append(list(current))
                return
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    current.append(num)
                    dfs(current)
                    used.remove(num)
                    current.pop()

        dfs([])
        return results