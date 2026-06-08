"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = {}
        def dfs(n):
            if not n:
                return None

            if n in visited:
                return visited[n]
            copy = Node(n.val)
            visited[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy
        return dfs(node)

        # time: O(V*E); V = height of node, E = avg neighbors of each node
        # space: O(1)














        # if not node:
        #     return None

        # oldToNew = {}
        # q = deque([node])

        # while q:
        #     cur = q.popleft()

        #     if cur not in oldToNew:
        #         oldToNew[cur] = Node(cur.val)

        #     for nei in cur.neighbors:
        #         if nei not in oldToNew:
        #             oldToNew[nei] = Node(nei.val)
        #             q.append(nei)

        #         oldToNew[cur].neighbors.append(oldToNew[nei])

        # return oldToNew[node]