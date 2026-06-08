class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)

        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])
        remaining = n

        while remaining > 2:
            size = len(leaves)
            remaining -= size

            for _ in range(size):
                leaf = leaves.popleft()
                nei = graph[leaf].pop()
                graph[nei].remove(leaf)

                if len(graph[nei]) == 1:
                    leaves.append(nei)

        return list(leaves)