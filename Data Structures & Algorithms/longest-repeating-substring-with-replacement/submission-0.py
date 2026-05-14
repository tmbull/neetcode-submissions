class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # with no replacements allowed:
        # iterate through the string
            # for each char, while s[n] == s[n-1], increment counter
            # when a new char is encountered, reset counter
            # with 2 replacements:
                # need to track last 3 chars
                    # track first index and # occurences
                    # 
        counts = defaultdict(int)
        result = 0
        l = 0
        for r in range(0, len(s)):
            counts[s[r]] += 1
            length = r - l + 1
            while length - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
                length = r - l + 1

            result = max(result, length)

        return result
        