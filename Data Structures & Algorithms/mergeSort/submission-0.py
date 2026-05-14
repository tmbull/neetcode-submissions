# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mSort(pairs, 0, len(pairs) - 1)

    def mSort(self, pairs, start, end) -> List[Pair]:
        if end - start + 1 <= 1:
            return pairs

        mid = (end + start) // 2
        
        self.mSort(pairs, start, mid)
        self.mSort(pairs, mid + 1, end)

        self.merge(pairs, start, mid, end)

        return pairs

    def merge(self, pairs, start, mid, end):
        left = list(pairs[start:mid + 1])
        right = list(pairs[mid + 1: end + 1])

        curr = start
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if right[j].key < left[i].key:
                pairs[curr] = right[j]
                j += 1
            else:
                pairs[curr] = left[i]
                i += 1
            curr += 1

        while i < len(left):
            pairs[curr] = left[i]
            i += 1
            curr += 1

        while j < len(right):
            pairs[curr] = right[j]
            j += 1
            curr += 1