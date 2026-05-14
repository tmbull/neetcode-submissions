# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qSort(pairs, 0, len(pairs) - 1)

        return pairs

    def qSort(self, pairs, s, e):
        if e - s + 1 <= 1:
            return

        pivot = e
        insert = s
        for i in range(s, e):
            if pairs[i].key < pairs[pivot].key:
                pairs[i], pairs[insert] = pairs[insert], pairs[i]
                insert += 1
            
        pairs[pivot], pairs[insert] = pairs[insert], pairs[pivot]

        self.qSort(pairs, s, insert - 1)
        self.qSort(pairs, insert + 1, e)