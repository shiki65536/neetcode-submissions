class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)


        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        res = 0
        visited = set()
        heap = [(0,0)]

        while len(visited) < N:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            res += weight 
            visited.add(node)

            for cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap,  (cost, nei))
        
        return res


















        # N = len(points)
        # adj = {i:[] for i in range(N)}
    
        # for i in range(N):
        #     x1, y1 = points[i]
        #     for j in range(i+1, N):
        #         x2, y2 = points[j]
        #         dist = abs(x1-x2) + abs(y1-y2)
        #         adj[i].append((dist, j))
        #         adj[j].append((dist, i))

        # res = 0
        # visited = set()
        # heap = [(0, 0)]

        # while len(visited) < N:
        #     weight, node = heapq.heappop(heap)
        #     if node in visited:
        #         continue
        #     res += weight
        #     visited.add(node)

        #     for cost, nei in adj[node]:
        #         if nei not in visited:
        #             heapq.heappush(heap, (cost, nei))
        
        # return res


