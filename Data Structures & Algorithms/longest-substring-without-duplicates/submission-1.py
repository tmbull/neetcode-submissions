class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # iterate through the string and keep track of char -> last index
        # when a duplicate is found, set current index to previously found index
        max_len = 0
        chars = set()
        l = 0
        for r, c in enumerate(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            max_len = max(max_len, r - l + 1)
            print(f"{c} {l} {r}")

        return max_len