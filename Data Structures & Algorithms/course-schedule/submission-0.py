class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for cse, pre in prerequisites:
            adj[cse].append(pre)
            indegree[pre] += 1
        
        queue = deque([])
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        finish = 0
        while queue:
            course = queue.popleft()
            finish += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return finish == numCourses
