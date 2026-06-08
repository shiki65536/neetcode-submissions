class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))  # (next, price)

        heap = [(0, src, 0)]  # (cost, node, edges_used)
        best = {}  # (node, edges_used) -> min cost

        while heap:
            cost, node, count = heapq.heappop(heap)
            if node == dst:
                return cost
            if count > k:
                continue
            state = (node, count)
            if state in best and cost > best[state]:
                continue
            best[state] = cost 
            for nxt, price in adj[node]:
                heapq.heappush(heap, (cost+price, nxt, count+1))

        return -1