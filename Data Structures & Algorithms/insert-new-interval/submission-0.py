class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # cases
        # new[end] < i[0][start]
        # new[start] > i[-1][end]
        # new[start] < i[start] < new[end] < i[end]
        # i[start] < new[start] <  i[end] < new[end]
        # i[start] < new[start] <  i[end] < new[end]
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
                
        res.append(newInterval)
        return res
