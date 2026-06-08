class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        heap = [(0, k)]
        visited = set()
        time = 0
        
        while heap:
            w, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            time = w

            for adj, weight in edges[n1]:
                # if adj not in visited:
                heapq.heappush(heap, (time+weight, adj))

        return time if len(visited) == n else -1

