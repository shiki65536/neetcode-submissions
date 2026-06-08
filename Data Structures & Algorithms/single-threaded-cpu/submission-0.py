class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((enq, proc, idx) for idx, (enq, proc) in enumerate(tasks))
        
        res = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)

        while heap or i < n:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(heap, (proc, idx))
                i += 1

            proc, idx = heapq.heappop(heap)
            time += proc
            res.append(idx)

        return res