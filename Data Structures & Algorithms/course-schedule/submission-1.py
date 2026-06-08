class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visiting = set()

        def dfs(c):
            if c in visiting:
                return False
            if pre_map[c] == []:
                return True

            visiting.add(c)
            for pre in pre_map[c]:
                if not dfs(pre):
                    return False
            visiting.remove(c)
            pre_map[c] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

