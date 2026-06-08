class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        output = []
        graph = defaultdict(list)
        to_user = {}

        # map
        for account in accounts:
            for i in range(1, len(account)):
                graph[account[i]].extend(account[1:])
                to_user[account[i]] = account[0]

        visited = set()

        # bfs
        for email in graph:
            if email in visited:
                continue
            
            q = deque([email])
            visited.add(email)
            group = []

            while q:
                node = q.popleft()
                group.append(node)

                for nei in graph[node]:
                    if nei in visited:
                        continue
                    q.append(nei)
                    visited.add(nei)

            user = to_user[email]
            
            output.append([user] + sorted(group))

        return output

       