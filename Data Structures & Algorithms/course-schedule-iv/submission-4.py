class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = [[] for _ in range(numCourses)]
        for pre, crs in prerequisites:
            graph[crs].append(pre)

        memo = {}

        def find(course):
            if course in memo:
                return memo[course]

            res = set()
            for pre in graph[course]:
                res.add(pre)
                res |= find(pre)

            memo[course] = res
            return res

        for course in range(numCourses):
            find(course)

        return [u in memo[v] for u, v in queries]
        ######
        graph = [[] for _ in range(numCourses)]
        ans = [[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            graph[crs].append(pre)
        
        def find(target):
            res = []
            for pre in graph[target]:
                if pre not in history:
                    history.add(pre)
                    res.append(pre)
                    res += find(pre)
            return res

        for crs, pre in enumerate(graph):
            history = set()
            for pre in graph[crs]:
                relation = find(pre)
                ans[crs].append(pre)
                ans[crs] += relation
        
        res = []

        for u, v in queries:
            if u in ans[v]:
                res.append(True)
            else:
                res.append(False)

        return res