class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))


        def bfs(start, end):
            if start not in graph:
                return -1
            if start == end:
                return 1.0
      
            q = deque(graph[start])
            visited = set()
            while q:
                node, value = q.popleft()
                for nei, val in graph[node]:
                    if nei in visited:
                        continue
                    val *= value
                    if nei == end:
                        return val
                    else:
                        q.append((nei, val))
                        visited.add(nei)
            return -1


        output = [bfs(s, e) for s, e in queries]

        return output