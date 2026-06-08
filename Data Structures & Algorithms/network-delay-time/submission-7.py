from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for source, target, time in times:
            adj[source].append((target, time))
        
        dist = {node: float("inf")  for node in range(1, n + 1)}
        dist[k] = 0

        queue = deque([(k, 0)])
        while queue:
            node, length = queue.popleft()
            if dist[node] < length:
                continue
            for target, time in adj[node]:
                if length + time < dist[target]:
                    dist[target] = length + time
                    queue.append((target, length + time))

        return max(dist.values()) if max(dist.values()) < float('inf') else -1
