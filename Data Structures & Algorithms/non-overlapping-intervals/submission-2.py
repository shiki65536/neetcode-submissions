class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or len(intervals) == 1:
            return 0
        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] <= intervals[i][0]:
                res.append(intervals[i])
            else:
                if res[-1][1] <= intervals[i][1]:
                    continue
                else:
                    res.pop()
                    res.append(intervals[i])
        
        return len(intervals) - len(res)