class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        for i in reversed(range(len(arr))):
            curr = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, curr)
        
        return arr