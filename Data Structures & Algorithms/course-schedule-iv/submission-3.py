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