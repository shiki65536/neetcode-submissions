"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        if len(intervals) == 1:
            return 1
        
        start = sorted([val.start for val in intervals])
        end = sorted([val.end for val in intervals])

        count = 0
        res = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res
