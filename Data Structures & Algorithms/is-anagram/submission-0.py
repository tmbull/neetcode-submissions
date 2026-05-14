class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        for c in s:
            chars[c] += 1

        for c in t:
            chars[c] -= 1

        for count in chars.values():
            if count != 0:
                return False

        return True