class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        last = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < last:
                res += 1
                last = min(last, interval[1])
            else:
                last = interval[1]
        
        return res