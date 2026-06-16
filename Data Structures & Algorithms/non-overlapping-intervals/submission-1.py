class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        res = [intervals[0]]
        for i, (start, end) in enumerate(intervals[1:]):
            lastEnd = res[-1][1]

            if lastEnd > start:
                intervals.remove(intervals[i])
                count += 1
            else:
                res.append([start,end])
        return count