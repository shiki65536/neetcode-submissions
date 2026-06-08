class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        self.count = 0
        visited = set()

        for cur, nei in edges:
            adj[cur].append(nei)
            adj[nei].append(cur)

        def bfs(node):
            if node in visited:
                return
            queue = deque([node])

            while queue:
                cur = queue.popleft()
                visited.add(cur)

                for nei in adj[cur]:
                    if nei not in visited:
                        queue.append(nei)
            self.count += 1

        for i in range(n):
            bfs(i)
        
        return self.count
