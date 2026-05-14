class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def combos(curr, i, total):
            if total == target:
                results.append(curr.copy())
                return
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            combos(curr, i + 1, total + candidates[i])

            curr.pop()
            ch = candidates[i]
            while i + 1 < len(candidates) and candidates[i + 1] == ch:
                i += 1
            combos(curr, i + 1, total)

        combos([], 0, 0)
        return results