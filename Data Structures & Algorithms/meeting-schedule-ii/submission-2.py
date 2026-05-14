"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # num days is equal to the max number of overlapping meetings
        # [(0,40),(5,10),(15,20)]
        if not intervals:
            return 0
        
        days = 0
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort()

        curr = 0
        for t, count in time:
            curr += count
            days = max(days, curr)
        
        return days