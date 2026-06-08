class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not numCourses:
            return []

        # graph = pre: [course, course]
        # blocker = course: int(number of prereqis)
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        blocker = [0] * numCourses
        for i in range(numCourses):
            for blocked in graph[i]:
                blocker[blocked] += 1

        # start find path with
        # visited
        # queue.appedn( course without blocker)
        queue = deque([])
        path = []
        for i in range(numCourses):
            if blocker[i] == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            path.append(course)

            for blocked in graph[course]:
                blocker[blocked] -= 1
                if blocker[blocked] == 0:
                    queue.append(blocked)

        # return path if numCourses == lne(visited) else []
        return path if numCourses == len(path) else []
        # time: O(V + E)
        # space: O(V + E) + O(V)
