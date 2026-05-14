class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # calculate counts for each char in s and t
        # start from left and right
        # if s[l] not in t or count_s[l] > count_t[l] increment l
        # do the same with r
        # loop while r - l + 1 >= len(t) and one of above holds true
        if len(s) < len(t):
            return ""
        
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)
        for c in s:
            counts_s[c] += 1
        for c in t:
            counts_t[c] += 1

        l = 0
        r = len(s) - 1
        while r - l + 1 > len(t):
            if counts_s[s[l]] > counts_t[s[l]]:
                counts_s[s[l]] -= 1
                l += 1
            elif counts_s[s[r]] > counts_t[s[r]]:
                counts_s[s[r]] -= 1
                r -= 1
            else:
                break

        substr = True
        for k,v in counts_t.items():
            if counts_s[k] < v:
                substr = False
                break
        if substr:
            return s[l:r+1]

        return ""