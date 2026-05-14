class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        results = []
        def combos(i, curr):
            nonlocal results
            if len(curr) == len(digits):
                results.append(curr)
                return

            for ch in mapping[digits[i]]:
                combos(i+1, curr + ch)
        
        if digits:
            combos(0, "")
        return results