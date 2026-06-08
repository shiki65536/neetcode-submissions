class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        res = 0

        def bfs(row, col, count):
            q = deque([(row, col, count)])
            max_dist = 0
            while q:
                r, c, dist = q.popleft()
                num1 = matrix[r][c]
                max_dist = max(dist, max_dist)

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        num2 = matrix[nr][nc]
                        if num2 > num1:
                            q.append((nr, nc, dist+1))
            return max_dist
        
        for i in range(rows):
            for j in range(cols):
                res = max(res, bfs(i, j, 1))

        return res


