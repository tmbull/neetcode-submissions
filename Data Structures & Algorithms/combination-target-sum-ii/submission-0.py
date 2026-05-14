class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def combos(curr, i):
            if sum(curr) == target:
                results.append(curr.copy())
                return
            if i >= len(candidates):
                return

            curr.append(candidates[i])
            combos(curr, i + 1)

            curr.pop()
            ch = candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == ch:
                i += 1
            combos(curr, i + 1)

        combos([], 0)
        return results