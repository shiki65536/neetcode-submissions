class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r: int, c: int) -> int:
            if memo[r][c] != 0:
                return memo[r][c]

            best = 1
            cur = matrix[r][c]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > cur:
                    best = max(best, 1 + dfs(nr, nc))

            memo[r][c] = best
            return best

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans, dfs(i, j))
        return ans
        # rows, cols = len(matrix), len(matrix[0])
        # directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # res = 0

        # def bfs(row, col, count):
        #     q = deque([(row, col, count)])
        #     max_dist = 0
        #     while q:
        #         r, c, dist = q.popleft()
        #         num1 = matrix[r][c]
        #         max_dist = max(dist, max_dist)

        #         for dr, dc in directions:
        #             nr, nc = r+dr, c+dc
        #             if 0 <= nr < rows and 0 <= nc < cols:
        #                 num2 = matrix[nr][nc]
        #                 if num2 > num1:
        #                     q.append((nr, nc, dist+1))
        #     return max_dist
        
        # for i in range(rows):
        #     for j in range(cols):
        #         res = max(res, bfs(i, j, 1))

        # return res


