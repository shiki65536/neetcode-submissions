from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((t, v))
        
        visited = set ()
        heap = [(0, k)]
        t = 0

        while heap:
            wei, cur = heapq.heappop(heap)
            if cur in visited:
                continue
            
            res = wei
            visited.add(cur)

            for dist, nei in adj[cur]:
                if nei not in visited:
                    heapq.heappush(heap, (dist + wei, nei))
        
        return res if len(visited) ==n else -1

















        # adj = defaultdict(list)

        # for source, target, time in times:
        #     adj[source].append((target, time))
        
        # dist = {node: float("inf")  for node in range(1, n + 1)}
        # dist[k] = 0

        # queue = deque([(k, 0)])
        # while queue:
        #     node, length = queue.popleft()
        #     if dist[node] < length:
        #         continue
        #     for target, time in adj[node]:
        #         if length + time < dist[target]:
        #             dist[target] = length + time
        #             queue.append((target, length + time))

        # return max(dist.values()) if max(dist.values()) < float('inf') else -1
