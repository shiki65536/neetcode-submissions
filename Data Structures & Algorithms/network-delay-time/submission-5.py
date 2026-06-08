from collections import deque

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for cur, nei, time in times:
            if cur not in adj:
                adj[cur] = []
            adj[cur].append((nei, time))
        
        queue = deque([(k)])
        # Track shortest distance to each node
        dist = {k: 0}

        while queue:
            idx = queue.popleft()
            for nei, time in adj.get(idx, []):
                new_dist = dist[idx] + time
                if nei not in dist:
                    dist[nei] = new_dist
                    queue.append(nei)
                elif new_dist < dist[nei]:
                    dist[nei] = new_dist
                    queue.append(nei)
        
        return max(dist.values()) if len(dist) == n else -1
        



