class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals or not queries:
            return [-1]
        
        intervals.sort(key=lambda x:x[0])
        res = []

        def find(q):
            mini = float("INF")

            for start, end in intervals:
                if start <= q <= end:
                    mini = min(mini, end-start+1)

            return mini if mini != float("INF") else -1

        for query in queries:
            ans = find(query)
            res.append(ans)

        return res
