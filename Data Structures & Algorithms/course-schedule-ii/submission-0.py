class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        need = [0] * numCourses
        unlock = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            unlock[pre].append(crs)
            need[crs] += 1
        
        res = []

        queue = deque([i for i in range(numCourses) if need[i] == 0])

        while queue:
            pre = queue.popleft()
            res.append(pre)

            for course in unlock[pre]:
                need[course] -= 1
                if need[course] == 0:
                    queue.append(course)

        return res if len(res) == numCourses else []
