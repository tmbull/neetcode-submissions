class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        # contains a permutation means
            # s2 contains all characters in s1 in any order, but they must be 
            # contiguous
            # how to track chars in any order... 
            # iterate through s1 and calculate counts of each char
            # iterate a fixed window len(s1) through s2
            # if counts_s1 == counts_s2, return true. Otherwise, return false

        s1_counts = defaultdict(int)
        s2_counts = defaultdict(int)
        for c in s1:
            s1_counts[c] += 1

        for i in range(len(s1)):
            s2_counts[s2[i]] += 1

        for r in range(len(s1), len(s2)):
            if s1_counts.items() <= s2_counts.items():
                return True
            l = r - len(s1)
            s2_counts[s2[l]] -= 1
            s2_counts[s2[r]] += 1
            print(f"{s1_counts} > {s2_counts}")

        return s1_counts.items() <= s2_counts.items()
